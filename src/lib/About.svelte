<script>
    import Navbar from "./Navbar.svelte";
</script>

<style>
@font-face {
    font-family: "valko";
    src: url("src/fonts/VALKOCAPELARegular.ttf") format("truetype");
}
* {
    font-family: "valko";
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    color:white;
}
main {
    background-color: black;
    height: 100vh;
}

.container {
  display: grid;
  grid-template-columns: 1fr 1fr;


}

.left, .right {
margin-top: 20vh;
}

.left {
display:grid;
  justify-content: end;
  margin-right: 50px;
}

.left img {
  width: 35vw;
  max-width: 500px;
  border-radius: 10px;
}

.right {
width: 30vw;
}

.title {
font-size: 80px;
font-weight: bold;
margin-bottom: 20px;
color: #45dfa2;
}

.content {
text-transform: uppercase;
font-size: 24px;
}

</style>


<main>

<Navbar/>

<div class="container">

<div class="left">

  <img src="src\assets\about.jpeg" alt="">

</div>

<div class="right">
<div class="title">
ABOUT
</div>

<div class="content">
WHAT- An Fashion Recommender using AI to generate outfit when you don't know what to wear. We using ChatGPT and Stable Diffusion which promise to bring the best experience.
</div>

</div>

</div>


</main>
