/**
* Filename : Uage_DayOfMonthInYear.java
* Author : DengPengFei
* Creation time : ����4:25:35 - 2020��5��6��
*/
package flowControl;
import java.util.Scanner;

/**
 *    Java��Ŀʵս���ж�����ƽ�겢���ĳ�µ�����
 */

public class Uage_DayOfMonthInYear {

	public static void demo() {
		
		Scanner input = new Scanner(System.in);
		
		System.out.println("��������ݣ�");
		
		int year = input.nextInt();
		
		System.out.println("�������·ݣ�");
		
		int month = input.nextInt();
		
		boolean isRunYear;
		
		int day = 0;
		
		// �ж��Ƿ�Ϊ���� 1���ܱ� 4 �����Ҳ��ܱ�100���� 2���ܱ�400������
		if (year % 4 == 0 && year % 100 != 0 || year % 400 == 0) {
			isRunYear = true;
		}else {
			isRunYear = false;
		}
		
		// �ж��·�
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
			System.out.println(year+"��"+month+"��һ��"+day+"�� ��");
			
		}else {
			System.out.println("��������·�����");
		}
		input.close();

	}
	
	public static void main(String[] arge) {
		demo();
		
	}
	
}
