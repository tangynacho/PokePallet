/* eslint-disable */

import Vue from "vue";
import Router from "vue-router";
import Home from "@/components/Home";
import New from "@/components/templates/NewPage";
import Ratings from "@/components/Ratings";
import Pallet from "@/components/Pallet";
import Supported from "@/components/Supported";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home
    },
    {
      path: "/newpage",
      name: "NewPage",
      component: New
    },
    {
      path: "/ratings",
      name: "Ratings",
      component: Ratings
    },
    {
      path: "/pallet",
      name: "Pallet",
      component: Pallet
    },
    {
      path: "/supported",
      name: "Supported",
      component: Supported
    }
  ]
});
