<template>
  <div>
    <Navbar />
    <Home />
  </div>
</template>

<script>
import Home from './components/Home.vue'
import Navbar from './components/Navbar.vue'

export default {
  components: {
    Home,
    Navbar
  }
}
</script>
