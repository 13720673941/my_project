/**
* Filename : Uage_AirTicketEnquiry.java
* Author : DengPengFei
* Creation time : ����4:54:23 - 2020��5��6��
*/
package flowControl;
import java.util.Scanner;

/**
 * ������Ŀ��
 * ĳ���չ�˾Ϊ��������Ĺ˿��Ƴ����Żݻ��ԭ���ķɻ�Ʊ��Ϊ 60000 Ԫ��
 * �ʱ��4~11 ��������ͷ�Ȳ� 9 �ۣ����ò� 8 �ۣ�1~3 �¡�12 �µ�����ͷ�Ȳ� 5 �ۣ����ò� 4 �ۣ����Ʊ�ļ۸�
 */

public class Uage_AirTicketEnquiry {

	public static void demo() {
		
		// ʵ����Scanner��
		Scanner input = new Scanner(System.in);
		
		// �����·ݱ���
		System.out.println("�����е�ʱ���Ǽ��·�(1~12)��");
		int month = input.nextInt();
		// ���崬�յȼ�����
		System.out.println("��ѡ�� ��ͷ�Ȳա� ���� �����òա� ��");
		String cabinType = input.next();
		
		// ԭ��Ĭ��Ϊ6000 ����
		final int originalPrice = 6000;
		// �ۿ۱���
		double discount = 0;
		boolean flag;
		
		// �ж��·�
		if (month >= 4 && month <= 11) {
			
			// ��������
			if (cabinType.equals("ͷ�Ȳ�")) {
				discount = 0.90;
			}else if (cabinType.equals("���ò�")) {
				discount = 0.80;
			}
			flag = true;
			
		}else if (month >= 1 && month <= 3 || month == 12) {
			
			// ��������
			if (cabinType.equals("ͷ�Ȳ�")) {
				discount = 0.50;
			}else if (cabinType.equals("���ò�")) {
				discount = 0.40;
			}
			flag = true;
			
		}else {
			flag = false;
			System.out.println("��������·����󣡣���");
		}
		input.close();
		
		// �����Ʊ�۸�
		if (flag) {
			System.out.println("�������Ļ�Ʊ�۸�Ϊ��"+(originalPrice*discount)+"Ԫ��");
		}
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo();
		
	}

}
