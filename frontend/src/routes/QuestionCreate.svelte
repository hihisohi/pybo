<script>
    import { push } from "svelte-spa-router"
    import fastapi from "../lib/api"
    import Error from "../components/Error.svelte"

    let error = {detail:[]}
    let subject = ''
    let content = ''

    function post_question(e) {
        e.preventDefault()

        let url = "/api/question/create"
        let params = {
            subject: subject,
            content: content
        }

        fastapi('post', url, params,
            (json) => {
                push("/")
            },
            (json_error) => {
                error = json_error
            }    
        )
    }
</script>

<h5>질문 등록</h5>
<Error error={error} />
<form method="post">
    <input type="text" bind:value="{subject}">
    <textarea row="10" bind:value={content}></textarea>
    <button type="submit" on:click="{post_question}">등록하기</button>
</form>