from config import load_config
from github_api import get_pull_requests, get_file_changes, add_comment_to_pull_request

def main():
    config = load_config()

    GITHUB_API_TOKEN = config.get("GITHUB_API_TOKEN")
    REPO_OWNER = config.get("REPO_OWNER")
    REPO_NAME = config.get("REPO_NAME")

    if GITHUB_API_TOKEN is None:
        raise Exception('GITHUB_API_TOKEN is not set')

    try:
        print("========================================")
        print("GitHub Repository Pull Request Processor")
        print("========================================")
        print(f"Repository Owner: {REPO_OWNER}")
        print(f"Repository Name: {REPO_NAME}")
        print("========================================\n")

        pull_requests = get_pull_requests(REPO_OWNER, REPO_NAME, GITHUB_API_TOKEN)
        print(f"Found {len(pull_requests)} pull requests in the repository.\n")

        for pr in pull_requests:
            print(f"Processing Pull Request #{pr['number']}: {pr['title']} (State: {pr['state']})")
            print("Fetching file changes...")
            file_names = get_file_changes(REPO_OWNER, REPO_NAME, pr['number'], GITHUB_API_TOKEN)
            print("File Changes:", file_names)
            print("Adding comment to the pull request...")
            comment = f"Testing PR #{pr['number']}: {pr['title']}"
            success = add_comment_to_pull_request(REPO_OWNER, REPO_NAME, pr['number'], comment, GITHUB_API_TOKEN)
            if success:
                print(f"Comment successfully added to Pull Request #{pr['number']}.\n")
            else:
                print(f"Failed to add comment to Pull Request #{pr['number']}.\n")
            print("------------------------------------------------------")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
