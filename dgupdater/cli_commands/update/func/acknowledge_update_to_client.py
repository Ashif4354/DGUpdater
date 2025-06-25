from os import system

def acknowledge_update_to_client() -> None:
    system('cls')

    print("✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅")
    print("✅✅  🙌 Updated to the latest version. Restart the application to see the changes. 🙌  ✅✅")
    print('✅✅  🙌 In Tamil: "Update Mudinjiduchu da. App-a restart pannu". 🙌                    ✅✅')
    print("✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅")

    input("\nPress Enter or close this window to continue...")


if __name__ == "__main__":
    acknowledge_update_to_client()