from datetime import datetime
import requests

from config import TOKEN, FORMAT_DATE_FROM, FORMAT_DATE_TO, PROJECTS_ID, URL_GITLAB


def get_last_deploy_on_stand_for_project(project_id: int = 190, stand_name: str = 'qa3') -> dict:
    s = requests.Session()

    if not TOKEN.get('PRIVATE-TOKEN', None):
        raise ValueError('Не указан GitLab Token!')

    url_request = f'{URL_GITLAB}/api/v4/projects/{project_id}/deployments?environment={stand_name}&status=success&sort=desc'

    response = s.get(url_request, headers=TOKEN)

    if response.status_code != 200:
        raise SystemExit(f'Server response {response.status_code}: {response.json()}')

    data = response.json()

    return data[0] if data else {}


def get_last_deploy_on_stand_for_all_projects(stand_name: str = 'qa3') -> str:
    message = f'BRANCH ON {stand_name}\n' \
              f'{"PROJECT~":<12} | {"BRANCH~":<10} | {"USER DEPLOYED~":<17} | FINISH TIME~\n'

    for project_name, project_id in PROJECTS_ID.items():
        last_branch = get_last_deploy_on_stand_for_project(project_id, stand_name)

        try:
            branch_name = last_branch["deployable"]["ref"]
            finish_time = datetime.strptime(last_branch["deployable"]["finished_at"],
                                            FORMAT_DATE_FROM).strftime(FORMAT_DATE_TO)
            user_deploy = last_branch["deployable"]["user"]["name"]

            message += f'{project_name:<12} | {branch_name:<10} | {user_deploy:<17} | {finish_time}\n'
        except KeyError:
            message += f'{project_name:<12} | {"-":<10} | {"-":<17} | -\n'

    return message


STAND_NAME = 'test4'

if __name__ == "__main__":
    print(get_last_deploy_on_stand_for_all_projects(STAND_NAME))
