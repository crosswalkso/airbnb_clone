class GithubLogIn(APIView):
    def post(self, request):
        code = request.data.get("code")
        access_token = requests.post(
            f"https://github.com/login/oauth/access_token?code={code}&client_id=54c6b7dbb39c88e1e0b8&client_secret={settings.GH_SECRET}",
            headers={"Accept": "application/json"},
        )
        print("---------------")
        print(access_token.json())
        access_token = access_token.json().get("access_token")
        user_data = requests.get(
            "https://api.github.com/user",
            headers={
                "Authorization": f"Bearer {access_token}",
                "Accept": "application/json",
            },
        )
        user_data = user_data.json()
