google.maps.__gjsload__('overlay', function(_){var Bx=function(a){this.h=a},Rna=function(){},Cx=function(a){a.Eq=a.Eq||new Rna;return a.Eq},Sna=function(a){this.Da=new _.Ni(function(){var b=a.Eq;if(a.getPanes()){if(a.getProjection()){if(!b.bp&&a.onAdd)a.onAdd();b.bp=!0;a.draw()}}else{if(b.bp)if(a.onRemove)a.onRemove();else a.remove();b.bp=!1}},0)},Tna=function(a,b){function c(){return _.Oi(e.Da)}var d=Cx(a),e=d.Jn;e||(e=d.Jn=new Sna(a));_.mb(d.Pa||[],_.af);var f=d.Za=d.Za||new _.Dv,g=b.__gm;f.bindTo("zoom",g);f.bindTo("offset",g);f.bindTo("center",
g,"projectionCenterQ");f.bindTo("projection",b);f.bindTo("projectionTopLeft",g);f=d.xv=d.xv||new Bx(f);f.bindTo("zoom",g);f.bindTo("offset",g);f.bindTo("projection",b);f.bindTo("projectionTopLeft",g);a.bindTo("projection",f,"outProjection");a.bindTo("panes",g);d.Pa=[_.M(a,"panes_changed",c),_.M(g,"zoom_changed",c),_.M(g,"offset_changed",c),_.M(b,"projection_changed",c),_.M(g,"projectioncenterq_changed",c)];c();b instanceof _.vf&&(_.Q(b,"Ox"),_.P(b,148440))},Xna=function(a){if(a){var b=a.getMap();
if(Una(a)!==b&&b&&b instanceof _.vf){var c=b.__gm;c.overlayLayer?a.__gmop=new Vna(b,a,c.overlayLayer):c.h.then(function(d){d=d.ja;var e=new Dx(b,d);d.vb(e);c.overlayLayer=e;Wna(a);Xna(a)})}}},Wna=function(a){if(a){var b=a.__gmop;b&&(a.__gmop=null,b.h.unbindAll(),b.h.set("panes",null),b.h.set("projection",null),b.m.Kd(b),b.j&&(b.j=!1,b.h.onRemove?b.h.onRemove():b.h.remove()))}},Una=function(a){return(a=a.__gmop)?a.map:null},Vna=function(a,b,c){this.map=a;this.h=b;this.m=c;this.j=!1;_.Q(this.map,"Ox");
_.P(this.map,148440);c.vd(this)},Yna=function(a,b){a.h.get("projection")!=b&&(a.h.bindTo("panes",a.map.__gm),a.h.set("projection",b))},Dx=function(a,b){this.C=a;this.m=b;this.h=null;this.j=[]};_.Ta(Bx,_.O);Bx.prototype.changed=function(a){"outProjection"!=a&&(a=!!(this.get("offset")&&this.get("projectionTopLeft")&&this.get("projection")&&_.Td(this.get("zoom"))),a==!this.get("outProjection")&&this.set("outProjection",a?this.h:null))};var Ex={};_.Ta(Sna,_.O);Ex.vd=function(a){if(a){var b=a.getMap();(Cx(a).cv||null)!==b&&(b&&Tna(a,b),Cx(a).cv=b)}};Ex.Kd=function(a){var b=Cx(a),c=b.Za;c&&c.unbindAll();(c=b.xv)&&c.unbindAll();a.unbindAll();a.set("panes",null);a.set("projection",null);b.Pa&&_.mb(b.Pa,_.af);b.Pa=null;b.Jn&&(b.Jn.Da.Ac(),b.Jn=null);delete Cx(a).cv};var Fx={};Vna.prototype.draw=function(){this.j||(this.j=!0,this.h.onAdd&&this.h.onAdd());this.h.draw&&this.h.draw()};Dx.prototype.dispose=function(){};Dx.prototype.Kb=function(a,b,c,d,e,f,g,h){var k=this.h=this.h||new _.Oq(this.C,this.m,function(){});k.Kb(a,b,c,d,e,f,g,h);a=_.A(this.j);for(b=a.next();!b.done;b=a.next())b=b.value,Yna(b,k),b.draw()};Dx.prototype.vd=function(a){this.j.push(a);this.h&&Yna(a,this.h);this.m.refresh()};Dx.prototype.Kd=function(a){_.pb(this.j,a)};Fx.vd=Xna;Fx.Kd=Wna;_.Te("overlay",{rs:function(a){if(a){(0,Ex.Kd)(a);(0,Fx.Kd)(a);var b=a.getMap();b&&(b instanceof _.vf?(0,Fx.vd)(a):(0,Ex.vd)(a))}},preventMapHitsFrom:function(a){_.pr(a,{be:function(b){_.kn(b.event.Ia)},Cc:function(b){return _.Vq(b)},Kh:function(b){return _.Wq(b)},kd:function(b){return _.Wq(b)},Gc:function(b){return _.Xq(b)}}).aj(!0)},preventMapHitsAndGesturesFrom:function(a){a.addEventListener("click",_.Xe);a.addEventListener("contextmenu",_.Xe);a.addEventListener("dblclick",_.Xe);a.addEventListener("mousedown",
_.Xe);a.addEventListener("mousemove",_.Xe);a.addEventListener("MSPointerDown",_.Xe);a.addEventListener("pointerdown",_.Xe);a.addEventListener("touchstart",_.Xe);a.addEventListener("wheel",_.Xe)}});});
