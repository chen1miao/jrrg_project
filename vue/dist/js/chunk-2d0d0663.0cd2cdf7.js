(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0d0663"],{"688c":function(t,e,s){"use strict";s.r(e);var i=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",[t._m(0),s("div",{staticStyle:{float:"left"}},[s("div",{staticStyle:{float:"left",width:"833px","line-height":"68px",color:"#333","font-size":"24px","text-align":"center","margin-bottom":"10px"}},[t._v(t._s(t.goods.title))]),s("div",{staticStyle:{"text-align":"center","font-size":"12px"}},[t._v("发布时间："+t._s(t.goods.publishertime)+" 作者："+t._s(t.goods.publisher)+" 来源：校疫情防控应急指挥部")]),s("div",{staticStyle:{float:"left",width:"833px","margin-top":"20px","margin-left":"10px"}},[t._v(" "+t._s(t.goods.content))])])])},o=[function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",[s("img",{staticStyle:{float:"left"},attrs:{src:"https://www.scfai.edu.cn/newfy/3little.png",width:"306",height:"837px"}})])}],n={name:"Detail",data:function(){var t=this.$route.query.id;return{user:localStorage.getItem("user")?JSON.parse(localStorage.getItem("user")):null,goods:{},goodsId:t,buyNum:1,comments:[],dialogVisible:!1}},created:function(){var t=this;this.request.get("/epknowledge/"+this.goodsId).then((function(e){return t.goods=e.data}))},methods:{addCart:function(){var t=this;null==this.user&&(this.dialogVisible=!0),this.request.post("/cart",{goodsId:this.goodsId,num:this.buyNum,userid:this.user.id}).then((function(e){"200"===e.code?t.$message.success("加入购物车成功"):t.$message.error(e.msg)}))},toLogin:function(){this.dialogVisible=!1,this.$router.push("login")}}},r=n,a=s("2877"),l=Object(a["a"])(r,i,o,!1,null,"9a0bbcb2",null);e["default"]=l.exports}}]);
//# sourceMappingURL=chunk-2d0d0663.0cd2cdf7.js.map