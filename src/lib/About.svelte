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
    overflow: hidden;
}

.container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  position:absolute;
  z-index: 3;
  width: 100vw;


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



@keyframes rotate {
  from {
    rotate: 0deg;
  }

  50% {
    scale: 1 1.5;
  }

  to {
    rotate: 360deg;
  }
}

#blob {
  background-color: white;
  height: 34vmax;
  aspect-ratio: 1;
  position: absolute;
  left: 50%;
  top: 50%;
  translate: -50% -50%;
  border-radius: 50%;
  background: linear-gradient(to right, aquamarine, mediumpurple);
  animation: rotate 20s infinite;
  opacity: 0.8;
}

#blur {
  height: 100%;
  width: 100%;
  position: absolute;
  z-index: 2;
  backdrop-filter: blur(12vmax);
}
</style>

<div id="blob"></div>
<div id="blur"></div>
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
