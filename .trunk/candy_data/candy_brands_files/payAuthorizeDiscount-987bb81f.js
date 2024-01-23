var e,o,s,i,n,t;import{r,j as a,b as c}from"./jsx-runtime-258b25e2.js";import{u as m,F as u,A as d}from"./Authorize.module-37bc3236.js";import{u as l,U as p,A as g}from"./AnalyticsProvider-9615690f.js";import{g as f}from"./index-0138779c.js";import{C as h}from"./CountriesProvider-ae9bc0d7.js";import{E as j}from"./ErrorBoundary-8c3293dc.js";import{P as k}from"./PageLoaded-b88b5eae.js";import{T as v,a as C,b as S}from"./Spacing-753db42d.js";import{A as b}from"./analyticsContext-fdeffcb6.js";import"./fetch-e7ffda61.js";import{S as y,b as w,c as x}from"./account-fd84b88a.js";import{T as A}from"./constants-e9d40a88.js";import{A as P}from"./AuthorizeWithConsent-6ff8d712.js";import{u as _}from"./useAuthorizeTexts-2dd4e2fa.js";import{u as z,a as D,b as E,i as I}from"./usePostMessage-970fdbb5.js";import{S as T,f as U}from"./Account-d589aa08.js";import"./_commonjsHelpers-26303f2a.js";import"./Link-9886a32d.js";import"./index-a00e579d.js";import"./UserCard-a7cfbbd9.js";import"./Tooltip-7ee387ec.js";import"./Button-50dd3723.js";import"./CodeInput-4458d458.js";import"./AutoSubmitForm-566da833.js";import"./notifier-6206eee4.js";import"./monorail-75228f09.js";import"./tslib.es6-ba7e95a7.js";import"./events-3c6df96d.js";import"./index-5819a1d2.js";import"./useResizeObserver-e02b5b13.js";import"./ResizeObserver-80d14552.js";import"./Authorize-0fc86e32.js";import"./useIsPasskeysLoginSupported-3783cb45.js";import"./env-2e924548.js";import"./cookies-cfd7b9ff.js";import"./useIsPasskeysSupportedBrowser-c3399a9c.js";import"./Identity-df7dd669.js";import"./usePointOfSale-8a17368d.js";import"./Section-30bc4741.js";import"./Heading-314646c1.js";import"./Notification-5f6e7454.js";import"./UIContextProvider-025d22e4.js";import"./common-ca01f106.js";import"./ShopAuthInputField-ab160887.js";import"./Input-07d5e8b6.js";import"./FlagInput-334d16ac.js";import"./preload-helper-0c4d888d.js";import"./VerificationNotification-11e5e8fd.js";import"./exclamation-58267080.js";import"./AuthorizeConfirm-ef711eb5.js";const L="discount-code-save-error@myshopify.io",R=1500;function N({phoneCapture:e=!1,saveDiscountAt:o}){const{translate:s}=r.useContext(v),[i,n]=r.useState(!1),[t,c]=r.useState(!1),[u,d]=r.useState(null),p="never"===o,[g,f]=r.useState(!1),h=!e||"phone-consent-confirmed"===o&&u,{authToken:j,devMode:k,fullView:C,flowVersion:S,setAuthToken:N,targetOrigin:B,updateConfirmParams:F,shopPermanentDomain:M,submittedEmail:O,setSubmittedEmail:V}=m(),{analyticsTraceId:q}=l(),{messageRestarted:H,messageEmailSubmitted:K,messageError:W,messageLoginComplete:Q,messageResized:G,messageShopUserMatched:J,messageLoaded:X,messageProcessing:Y,messageCloseRequested:Z,messageDiscountSaved:$,messageVerificationSuccess:ee,messageAuthorizeStepChanged:oe}=function(e,o){const s=z(e,o);return{...D(e,o),messageDiscountSaved:s("discount_saved")}}(B,C);E({onEscapeKeypress:Z});const se=r.useCallback((async({discountCode:e})=>{if(I(e)){Y({status:x.Loading,message:s("confirm.discount.processing_loading")});try{if(k){if(O===L)throw new T({});await new Promise((e=>{setTimeout((()=>{console.debug("[Pay] Discount saved (stubbed for dev mode)."),e()}),R)}))}else{const o=await U({code:e,shopify_domain:M,analytics_trace_id:q,flow:b.Discount,flow_version:S,session_token:j});N(o.token)}f(!0),Y({status:x.Success,message:s("confirm.discount.processing_success")}),$()}catch(o){W({email:O,code:y.ServerError,message:w.DiscountSaveFailed})}}else W({email:O,code:y.NoDiscountReceived,message:w.InvalidDiscount})}),[q,j,k,S,W,$,Y,N,M,O,s]);function ie(){Q({email:O,loggedIn:!1})}r.useEffect((()=>{function e(e){const{type:o,...s}=e.data;switch(o){case"emailsubmitted":!function({email:e,hideChange:o}){"string"==typeof e&&(V(e),n(Boolean(o)))}(s);break;case"savediscount":se(s);break;case"phoneshareconsentreceived":!function({skipDiscountSaving:e,consented:o}){e&&f(!0),F({phone_share_consent:String(o)}),d(Boolean(o))}(s)}}return window.addEventListener("message",e),()=>window.removeEventListener("message",e)}),[O,V,W,F,s,$,Y,se]);const{authorizeTexts:ne}=_();const te=r.useMemo((()=>{const o=[{condition:p||g,error:"Discount must be saved before confirming."}];return e&&o.push({condition:null!==u,error:"Phone share consent must be received before confirming."}),o}),[g,p,e,u]),re={disallowUserChange:i,trackingSetup:{context:A.LoginWithShopDiscount},confirmConditions:te,hidden:!t,texts:ne,showShopLogo:!1,disallowOneClickPersonalizationConsent:!0,onLoaded:function({userFound:e,logoSrc:o,personalizeConsentChallenge:i}){X({userFound:e,logoSrc:o,loginTitle:s("confirm.discount.login_title"),personalizeConsentChallenge:i})},onResized:G,onUserFound:function({userCookieExists:e,maskedPhoneNumber:o,personalizeConsentChallenge:s}){(e||s)&&(t||(c(!0),J({userCookieExists:e,maskedPhoneNumber:o,description:"",personalizeConsentChallenge:s})))},onUserNotFound:ie,onRestarted:function(){H(),V(""),c(!1)},onUserVerification:function({userRecord:e,newUser:o}){o||(J({userCookieExists:!1,description:s("confirm.discount.login_sms_description",{phoneNumber:e.phone_number||""}),maskedPhoneNumber:e.phone_number}),c(!0))},onCaptchaChallenge:function(e){W({email:e,code:y.UserBlocked,message:w.CaptchaChallenge}),Q({email:e,loggedIn:!1})},onUserConfirm:function(e){ee({email:e}),K({email:e})},onConfirmProcessing:function({email:e}){Y({status:x.Loading,email:e,...h&&{message:s("confirm.discount.processing_loading")}})},onConfirmSuccess:function({email:e}){Y({status:x.Success,email:e,...h&&{message:s("confirm.discount.processing_success")}})},onTokenReturned:function(e){Q({...e,loggedIn:!0})},onAuthorizeStepChanged:oe,onCancel:ie,onError:function(e){W(e),Q({email:e.email,loggedIn:!0})}};return a.jsx(P,{...re})}const B=f("analytics-trace-id"),F=f("authentication-level-required"),M=f("client"),O=f("confirm-params"),V=null==(e=f("dev-mode"))?void 0:e.toString(),q=f("dictionary"),H=null==(o=f("flow-version"))?void 0:o.toString(),K=f("full-view"),W=f("shop-permanent-domain"),Q=null==(s=f("target-origin-url"))?void 0:s.toString(),G=f("user"),J=Boolean(f("phone-capture")),X=null==(i=f("save-discount-at"))?void 0:i.toString(),Y=null==(n=f("uniq-token"))?void 0:n.toString(),Z=null==(t=f("visit-token"))?void 0:t.toString(),$={uiSection:p.AuthorizeDiscount,clientUuid:M.uuid,analyticsTraceId:B,...G&&{shopAccountUuid:G.shop_account_uuid}},ee={authenticationLevelRequired:F,client:M,confirmParams:O,devMode:V,flow:u.Discount,flowVersion:H,fullView:K,hideCopy:!0,shopPermanentDomain:W,signUpEnabled:!1,targetOrigin:Q,uniqToken:Y,user:G,visitToken:Z};var oe;oe=document.getElementById("app"),c.render(a.jsx(j,{bugsnagApiKey:window.ShopifyPay.Config.bugsnagApiKey,sectionName:"AuthorizeDiscount",children:a.jsx(g,{...$,children:a.jsx(k,{origin:"authorize_discount",children:a.jsx(C,{dictionary:q,children:a.jsx(S,{children:a.jsx(h,{children:a.jsx(d,{...ee,children:a.jsx(N,{phoneCapture:J,saveDiscountAt:X})})})})})})})}),oe);
