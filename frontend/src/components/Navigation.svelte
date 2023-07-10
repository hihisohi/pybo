<script>
    import { link } from 'svelte-spa-router'
    import { page } from '../lib/store'

    let navLinks = [
        ['회원가입', '/join'], 
        ['로그인', '/login']
    ]
</script>

<div id="header" class="fixed px-12 py-4 flex items-center">
    <a use:link href="/" on:click="{() => {$page = 0}}" class="w-40 text-xl font-bold text-indigo-600 mr-10">
        <img src="./images/pybo_logo.png" class="mx-full">
    </a>
    <nav>
        <ul class="flex">
            {#each navLinks as [title, url]}
            <li class="px-4"><a use:link href="{url}" class="text-indigo-800 font-bold">{title}</a></li>
            {/each}
        </ul>
    </nav>
</div>
