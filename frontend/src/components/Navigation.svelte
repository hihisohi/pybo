<script>
    import { link } from 'svelte-spa-router'
    import { page } from '../lib/store'

    let navLinks = [
        ['회원가입', '/join'], 
        ['로그인', '/login']
    ]
</script>

<div id="header" class="px-12 py-4 flex">
    <a use:link href="/" on:click="{() => {$page = 0}}" class="text-xl font-bold text-indigo-500 mr-10">Pybo</a>
    <nav>
        <ul class="flex">
            {#each navLinks as [title, url]}
            <li class="px-4"><a use:link href="{url}" class="">{title}</a></li>
            {/each}
        </ul>
    </nav>
</div>
