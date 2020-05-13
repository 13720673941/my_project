/**
* Filename : Uage_DayOfMonthInYear.java
* Author : DengPengFei
* Creation time : 下午4:25:35 - 2020年5月6日
*/
package flowControl;
import java.util.Scanner;

/**
 *    Java项目实战：判断闰年平年并输出某月的天数
 */

public class Uage_DayOfMonthInYear {

	public static void demo() {
		
		Scanner input = new Scanner(System.in);
		
		System.out.println("请输入年份：");
		
		int year = input.nextInt();
		
		System.out.println("请输入月份：");
		
		int month = input.nextInt();
		
		boolean isRunYear;
		
		int day = 0;
		
		// 判断是否为闰年 1、能被 4 整除且不能被100整出 2、能被400整出的
		if (year % 4 == 0 && year % 100 != 0 || year % 400 == 0) {
			isRunYear = true;
		}else {
			isRunYear = false;
		}
		
		// 判断月份
		if (month > 0 && month < 13) {
			if (month != 2) {
				switch (month) {
				case 1:
				case 3:
				case 5:
				case 7:
				case 8:
				case 10:
				case 12:
					day = 31;
					break;
				case 4:
				case 6:
				case 9:
				case 11:
					day = 30;
					break;
				default:
					break;
				}
			}else {
				if (isRunYear) {
					day = 29;
				}else {
					day = 28;
				}
			}
			System.out.println(year+"年"+month+"月一共"+day+"天 。");
			
		}else {
			System.out.println("您输入的月份有误！");
		}
		input.close();

	}
	
	public static void main(String[] arge) {
		demo();
		
	}
	
}
