<script>
    import womanImage from "./assets/landing.png";
    import rectangle1 from "./assets/Rectangle 1.png";
    import rectangle2 from "./assets/Rectangle 2.png";
    import rectangle3 from "./assets/Rectangle 3.png";
    import Navbar from "./lib/Navbar.svelte";
    import { fly } from 'svelte/transition';
    import { onMount } from 'svelte';

    let flyIn = false;

    onMount(() => {
    flyIn = true;
    });


</script>

<main>
    <div class="background">
        <img class="partial-background background1" src={rectangle1} alt="" />
        <img class="partial-background background2" src={rectangle2} alt="" />
        <img class="partial-background background3" src={rectangle3} alt="" />
        {#if flyIn}
        <img transition:fly="{{y: 150, duration: 1500 }}" class="woman" src={womanImage} alt="" />
        {/if}
        <Navbar />
        {#if flyIn}
        <div class="intro" transition:fly="{{ y: 150, duration: 2500 }}">
            <div class="title">AI Fashion Recommendation</div>
            <div class ="des">
                Our website offers personalized style advice based on the latest trends using AI. featuring
                top fashion brands and Focused on hottest fashion trends.
            </div>
            <button>Get started</button>
        </div>
        {/if}
    </div>
</main>

<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: "Valkocapela";
    }
    .background {
        display: flex;
        position: relative;
        z-index: 0;
        /* height: 100vh; */
    }
    .background1 {
        width: 27vw;
    }
    .background2 {
        width: 57vw;
    }
    .background3 {
        width: calc(100vw - 27vw - 57vw);
    }

    .partial-background {
        height: 100vh;
        display: inline;
        /* width: 50%; */
    }
    .woman {
        left: 10vw;
        position: absolute;
        z-index: 1;
        height: 100vh;
        mix-blend-mode: normal;
        filter: drop-shadow(-34px 21px 15px rgba(0, 0, 0, 0.15));
    }
    .intro {
        color: white;
        width: 27vw;
        position: absolute;
        top: 50vh;
        left: 50vw;
        text-transform: uppercase;
    }
    .intro .title {
        font-size: xx-large;
    }
    .intro button {
        width: 27vw;
        background-color: #eb6468;
        color: white;
        border: none;
        height: 5vh;
    }
    .title {
    margin-bottom: 1vh;
    }

    .des {
    margin-bottom: 2vh;
    cursor: pointer;
    }
</style>
