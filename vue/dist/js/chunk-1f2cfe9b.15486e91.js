(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-1f2cfe9b"],{"87bd":function(t,e,i){"use strict";i.r(e);var a=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",[i("div",{staticStyle:{margin:"10px 0"}},[t._m(0),i("div",{staticStyle:{float:"right",width:"872px","min-height":"658px"}},[i("div",{staticStyle:{float:"left",width:"870px","padding-left":"1px",border:"#eeeeee 1px solid","margin-bottom":"14px","min-height":"658px"}},[i("ul",{staticStyle:{float:"left","line-height":"38px",color:"#7d7c7c","padding-left":"18px"}},[t._l(t.goods,(function(e){return i("li",{key:e.id,on:{click:function(i){return t.$router.push("/front/notificationDeatil?id="+e.id)}}},[i("span",{staticStyle:{"font-size":"14px"}},[t._v(t._s(e.title))]),i("span",{staticStyle:{position:"absolute",right:"250px","font-size":"14px"}},[t._v(t._s(e.publishertime))])])})),i("div",{staticStyle:{padding:"10px 0"}},[i("el-pagination",{attrs:{background:"","current-page":t.pageNum,"page-sizes":[4,8,12],"page-size":t.pageSize,layout:"total, prev, pager, next",total:t.total},on:{"size-change":t.handleSizeChange,"current-change":t.handleCurrentChange}})],1)],2)])])])])},n=[function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",[i("img",{staticStyle:{float:"left"},attrs:{src:"https://www.scfai.edu.cn/newfy/3little.png",width:"306",height:"837px"}})])}],o=(i("b0c0"),{name:"FrontHome",data:function(){return{lun:[],files:[],goods:[],pageNum:1,pageSize:20,total:0,searchInput:""}},created:function(){this.load()},methods:{load:function(){var t=this;this.request.get("/lun").then((function(e){t.lun=e.data})),this.request.get("/notification/page",{params:{pageNum:this.pageNum,pageSize:this.pageSize,name:this.name}}).then((function(e){t.goods=e.data.records,t.total=e.data.total}))},handleSizeChange:function(t){this.pageSize=t,this.load()},handleCurrentChange:function(t){this.pageNum=t,this.load()},searchProduct:function(){var t=this;this.request.get("/notification/page",{params:{pageNum:this.pageNum,pageSize:this.pageSize,name:this.searchInput}}).then((function(e){t.goods=e.data.records,t.total=e.data.total}))}}}),s=o,l=(i("c6bf"),i("2877")),c=Object(l["a"])(s,a,n,!1,null,null,null);e["default"]=c.exports},"8e74":function(t,e,i){},c6bf:function(t,e,i){"use strict";i("8e74")}}]);
//# sourceMappingURL=chunk-1f2cfe9b.15486e91.js.map