/**
* Filename : Uage_FindJsFileName.java
* Author : DengPengFei
* Creation time : 下午4:25:59 - 2020年5月21日
*/
package JavaString;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 *  查找 js 文件
 *
 */

public class Uage_FindJsFileName {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		// 原始字符串
		
		String str = "<!DOCTYPE html><html lang=en><head><meta charset=utf-8><meta http-equiv=X-UA-Compatible content=\"IE=edge\"><meta name=viewport content=\"width=device-width,initial-scale=1\"><link rel=icon href=favicon.ico><title>超级物业</title><link rel=icon href=./favicon.ico type=image/x-icon><link rel=stylesheet href=./asset/default/css/font-awesome.min.css><link rel=stylesheet href=./styles/iview.css><link rel=stylesheet href=./asset/default/css/subject.css><link rel=stylesheet href=./asset/default/css/main.css><link rel=stylesheet href=css/app.77aa4fd0.css><script src=\"https://api.map.baidu.com/api?v=3.0&ak=EGvswWF8mSc79ayXrodAKyWXx6MwCi4H\"></script><script src=https://cdn.51shouhou.cn/js/vue.min.js></script><script src=https://cdn.51shouhou.cn/js/iview4.min.js></script><script src=https://cdn.51shouhou.cn/js/vuex.min.js></script><script src=https://cdn.51shouhou.cn/js/moment.min.js></script><link href=css/chunk-0506a909.a292fc4c.css rel=prefetch><link href=css/chunk-27e6e819.5729711d.css rel=prefetch><link href=css/chunk-2d0f92b0.956ccaa6.css rel=prefetch><link href=css/chunk-2dd95996.2c8e7519.css rel=prefetch><link href=css/chunk-4373ee3e.c2896a93.css rel=prefetch><link href=css/chunk-45d798c4.5105a276.css rel=prefetch><link href=css/chunk-4a29065a.7204ce1e.css rel=prefetch><link href=css/chunk-5aec85a8.e8cac78f.css rel=prefetch><link href=css/chunk-5b413df7.2c8e7519.css rel=prefetch><link href=css/chunk-bbfa7e5c.e6db8bd9.css rel=prefetch><link href=js/chunk-04646519.3d7a5038.js rel=prefetch><link href=js/chunk-0506a909.3788ab91.js rel=prefetch><link href=js/chunk-1592ccde.e060ebd6.js rel=prefetch><link href=js/chunk-17f0b85a.3f6c34f3.js rel=prefetch><link href=js/chunk-1feecca2.35d7289f.js rel=prefetch><link href=js/chunk-27e6e819.66247473.js rel=prefetch><link href=js/chunk-2d0ab8d5.ee2eefda.js rel=prefetch><link href=js/chunk-2d0b28f6.584f29ec.js rel=prefetch><link href=js/chunk-2d0b37d1.a5fef48a.js rel=prefetch><link href=js/chunk-2d0b5986.4a6425aa.js rel=prefetch><link href=js/chunk-2d0b93f7.1f75dc6f.js rel=prefetch><link href=js/chunk-2d0bac1b.80346224.js rel=prefetch><link href=js/chunk-2d0bcea0.77699adb.js rel=prefetch><link href=js/chunk-2d0bcec4.9aae4b95.js rel=prefetch><link href=js/chunk-2d0c22be.20f410bc.js rel=prefetch><link href=js/chunk-2d0cb71e.e4d6ebd7.js rel=prefetch><link href=js/chunk-2d0d2b14.6909db9c.js rel=prefetch><link href=js/chunk-2d0d721b.25408af1.js "
				+ "rel=prefetch><link href=js/chunk-2d0d83d6.b77b9dd0.js rel=prefetch><link href=js/chunk-2d0e543d.18883885.js rel=prefetch><link href=js/chunk-2d0e5ad9.ec0da67e.js rel=prefetch><link href=js/chunk-2d0e5d65.c92bbedc.js rel=prefetch><link href=js/chunk-2d0e5d80.138eb2a4.js rel=prefetch><link href=js/chunk-2d0e670f.418a08e9.js rel=prefetch><link href=js/chunk-2d0efd57.584b8b94.js rel=prefetch><link href=js/chunk-2d0f064f.addb23e0.js rel=prefetch><link href=js/chunk-2d0f0651.4f850ea6.js rel=prefetch><link href=js/chunk-2d0f92b0.7e71e875.js rel=prefetch><link href=js/chunk-2d210600.3ccd24a3.js rel=prefetch><link href=js/chunk-2d216851.3cc31e38.js rel=prefetch><link href=js/chunk-2d2179f1.6c3adb3b.js rel=prefetch><link href=js/chunk-2d21a821.b9b69e79.js rel=prefetch><link href=js/chunk-2d21d7c4.0d16725b.js rel=prefetch><link href=js/chunk-2d221dc5.54584f0c.js rel=prefetch><link href=js/chunk-2d22254a.c940e3e7.js rel=prefetch><link href=js/chunk-2d22497d.c6fbed91.js rel=prefetch><link href=js/chunk-2d225218.8769f4a1.js rel=prefetch><link href=js/chunk-2d2304d0.eff741ca.js rel=prefetch><link href=js/chunk-2d230ab5.db1095d5.js rel=prefetch><link href=js/chunk-2d230c66.37beca8b.js rel=prefetch><link href=js/chunk-2dd95996.4f1c718a.js rel=prefetch><link href=js/chunk-301af246.16f65ee9.js rel=prefetch><link href=js/chunk-4373ee3e.285faf22.js rel=prefetch><link href=js/chunk-45d798c4.dbc2494f.js rel=prefetch><link href=js/chunk-4a29065a.2555cc6d.js rel=prefetch><link href=js/chunk-5aec85a8.035b6c3c.js rel=prefetch><link href=js/chunk-5b413df7.434062ce.js rel=prefetch><link href=js/chunk-5e0e0863.607b8aa5.js rel=prefetch><link href=js/chunk-7240b3f6.3de4aec4.js rel=prefetch><link href=js/chunk-74864394.f4f96d8a.js rel=prefetch><link href=js/chunk-7eb3e5c9.3439f978.js rel=prefetch><link href=js/chunk-7fb78861.dad3d8e4.js rel=prefetch><link href=js/chunk-9399c6fe.3632dc59.js rel=prefetch><link href=js/chunk-9494e72e.1d83efc0.js rel=prefetch><link href=js/chunk-bbfa7e5c.36b98c15.js rel=prefetch><link href=js/chunk-c5bd1154.c2a21544.js rel=prefetch><link href=js/chunk-cded9d18.42c524e3.js rel=prefetch><link href=app.532894110ea0dfd1376a.js rel=preload as=script><link href=css/app.77aa4fd0.css rel=preload as=style><link href=js/chunk-vendors.d5833262.js rel=preload as=script><link href=css/app.77aa4fd0.css rel=stylesheet></head><body><div id=app></div><script src=js/chunk-vendors.d5833262.js></script>"
				+ "<script src=app.532894110ea0dfd1376a.js></script></body></html> js/chunk-.js";
		
		// 查找文件格式 ： js/chunk-2d0e543d.18883885.js
		Pattern pattern = Pattern.compile("href=(js\\/chunk\\-.*?\\.js)");
		Matcher matcher = pattern.matcher(str);
		
		while (matcher.find()) {
			System.out.println(matcher.group(1));
		}
	}

}
