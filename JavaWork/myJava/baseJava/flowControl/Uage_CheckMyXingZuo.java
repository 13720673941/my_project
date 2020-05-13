/**
* Filename : Uage_CheckMyXingZuo.java
* Author : DengPengFei
* Creation time : 下午5:59:20 - 2020年5月6日
*/
package flowControl;
import java.util.Scanner;

/*
 *   项目实战（根据生日日期计算你的星座）
 *   
 *   规则逻辑：
 *   白羊：0321~0420      天秤：0924~1023
 *   金牛：0421~0521      天蝎：1024~1122
 *	  双子：0522~0621          射手：1123~1221
 *	  巨蟹：0622~0722          摩羯：1222~0120
 *	  狮子：0723~0823          水瓶：0121~0219
 *	  处女：0824~0923          双鱼：0220~0320
 */

public class Uage_CheckMyXingZuo {
	
	// .switch实现计算星座功能
	public static void demo() {
		
		// 实例化类
		Scanner input = new Scanner(System.in);
		
		// 定义生日变量
		System.out.println("请输入您的生日：如(1月3日输 0103)");
		int birthday = input.nextInt();
		
		// 月份取整
		int month = birthday / 100;
		// 天数取余数
		int day = birthday % 100;
		// 星座
		String xingZuo = "";
		
		// 判断星座
		switch (month) {
		case 1:
			// 三元运算 OperationalCharacter.java 
			xingZuo = day > 20 ? "水瓶座":"摩羯座";
			break;
		case 2:
			xingZuo = day > 19 ? "双鱼座":"水瓶座";
			break;
		case 3:
			xingZuo = day > 20 ? "白羊座":"双鱼座";
			break;
		case 4:
			xingZuo = day > 20 ? "金牛座":"白羊座";
			break;
		case 5:
			xingZuo = day > 21 ? "双子座":"金牛座";
			break;
		case 6:
			xingZuo = day > 21 ? "巨蟹座":"双鱼座";
			break;
		case 7:
			xingZuo = day > 22 ? "狮子座":"巨蟹座";
			break;
		case 8:
			xingZuo = day > 23 ? "处女座":"狮子座";
			break;
		case 9:
			xingZuo = day > 23 ? "天枰座":"处女座";
			break;
		case 10:
			xingZuo = day > 23 ? "天蝎座":"天枰座";
			break;
		case 11:
			xingZuo = day > 22 ? "射手座":"天蝎座";
			break;
		case 12:
			xingZuo = day > 21 ? "摩羯座":"射手座";
			break;
		default:
			System.out.println("输入生日格式错误！！！");
			break;
		}
		
		System.out.println("您的星座是："+xingZuo);
		
		input.close();
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo();
	}

}
