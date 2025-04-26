import{j as e}from"./jsx-runtime.D_zvdyIk.js";import{r as u}from"./index.BVOCwoKb.js";import{c as i}from"./createLucideIcon.A48v_36S.js";/**
 * @license lucide-react v0.488.0 - ISC
 *
 * This source code is licensed under the ISC license.
 * See the LICENSE file in the root directory of this source tree.
 */const l=[["circle",{cx:"11",cy:"11",r:"8",key:"4ej97u"}],["path",{d:"m21 21-4.3-4.3",key:"1qie3q"}]],m=i("search",l);function f({onSearch:r,placeholder:a="Search...",className:o=""}){const[s,c]=u.useState(""),n=t=>{t.preventDefault(),r&&r(s)};return e.jsxs("form",{onSubmit:n,className:`flex w-full items-center space-x-2 ${o}`,children:[e.jsxs("div",{className:"relative flex-1",children:[e.jsx(m,{className:"absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground"}),e.jsx("input",{type:"text",placeholder:a,value:s,onChange:t=>c(t.target.value),className:"w-full px-3 py-2 pl-8 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"})]}),e.jsx("button",{type:"submit",className:"x-4 py-2 px-3 bg-gray-800 text-white rounded hover:bg-gray-800 transition-colors",children:"Buscar"})]})}export{m as S,f as a};
