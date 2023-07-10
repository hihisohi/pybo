<script>
    import { push } from 'svelte-spa-router'
    import fastapi from '../lib/api';
    import Error from "../components/Error.svelte"

    let error = {detail:[]}
    let username = ''
    let password1 = ''
    let password2 = ''
    let email = ''

    function post_user(e) {
        e.preventDefault()
        let url = "/api/user/create"
        let params = {
            username: username,
            password1: password1,
            password2: password2,
            email: email
        }
        fastapi('post', url, params,
            (json) => {
                push('/user-login')
            },
            (json_error) => {
                error = json_error
            }
        )
    }
</script>

<div>
    <h2 class="text-3xl font-bold text-center text-indigo-700">회원가입</h2>
    <form method="post">
        <div>
            <label for="">이름</label>
            <input type="text" class="input">
        </div>
        <div>
            <label for="">비밀번호</label>
            <input type="password" class="input">
        </div>
        <div>
            <label for="">비밀번호 확인</label>
            <input type="password" class="input">
        </div>
        <div>
            <label for="">이메일</label>
            <input type="text" class="input">
        </div>
    </form>
</div>