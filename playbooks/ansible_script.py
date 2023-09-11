
pip install ansible-runner

from ansible_runner import run

def run_ansible_playbook():
    r = run(playbook='path/to/your/playbook.yml', inventory='path/to/your/inventory.ini')

    if r.rc == 0:
        print("Playbook executed successfully.")
    else:
        print("Playbook failed with code:", r.rc)

if __name__ == '__main__':
    run_ansible_playbook()


