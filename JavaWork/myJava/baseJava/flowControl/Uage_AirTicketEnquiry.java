/**
* Filename : Uage_AirTicketEnquiry.java
* Author : DengPengFei
* Creation time : 下午4:54:23 - 2020年5月6日
*/
package flowControl;
import java.util.Scanner;

/**
 * 案例项目：
 * 某航空公司为吸引更多的顾客推出了优惠活动。原来的飞机票价为 60000 元，
 * 活动时，4~11 月旺季，头等舱 9 折，经济舱 8 折；1~3 月、12 月淡季，头等舱 5 折，经济舱 4 折，求机票的价格。
 */

public class Uage_AirTicketEnquiry {

	public static void demo() {
		
		// 实例化Scanner类
		Scanner input = new Scanner(System.in);
		
		// 定义月份变量
		System.out.println("您出行的时间是几月份(1~12)：");
		int month = input.nextInt();
		// 定义船舱等级变量
		System.out.println("您选择 “头等舱” 还是 “经济舱” ？");
		String cabinType = input.next();
		
		// 原价默认为6000 常量
		final int originalPrice = 6000;
		// 折扣变量
		double discount = 0;
		boolean flag;
		
		// 判断月份
		if (month >= 4 && month <= 11) {
			
			// 船舱类型
			if (cabinType.equals("头等舱")) {
				discount = 0.90;
			}else if (cabinType.equals("经济舱")) {
				discount = 0.80;
			}
			flag = true;
			
		}else if (month >= 1 && month <= 3 || month == 12) {
			
			// 船舱类型
			if (cabinType.equals("头等舱")) {
				discount = 0.50;
			}else if (cabinType.equals("经济舱")) {
				discount = 0.40;
			}
			flag = true;
			
		}else {
			flag = false;
			System.out.println("您输入的月份有误！！！");
		}
		input.close();
		
		// 输出机票价格
		if (flag) {
			System.out.println("您所定的机票价格为："+(originalPrice*discount)+"元！");
		}
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo();
		
	}

}
