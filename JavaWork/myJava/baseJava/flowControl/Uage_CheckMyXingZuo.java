/**
* Filename : Uage_CheckMyXingZuo.java
* Author : DengPengFei
* Creation time : ����5:59:20 - 2020��5��6��
*/
package flowControl;
import java.util.Scanner;

/*
 *   ��Ŀʵս�������������ڼ������������
 *   
 *   �����߼���
 *   ����0321~0420      ��ӣ�0924~1023
 *   ��ţ��0421~0521      ��Ы��1024~1122
 *	  ˫�ӣ�0522~0621          ���֣�1123~1221
 *	  ��з��0622~0722          Ħ�ɣ�1222~0120
 *	  ʨ�ӣ�0723~0823          ˮƿ��0121~0219
 *	  ��Ů��0824~0923          ˫�㣺0220~0320
 */

public class Uage_CheckMyXingZuo {
	
	// .switchʵ�ּ�����������
	public static void demo() {
		
		// ʵ������
		Scanner input = new Scanner(System.in);
		
		// �������ձ���
		System.out.println("�������������գ���(1��3���� 0103)");
		int birthday = input.nextInt();
		
		// �·�ȡ��
		int month = birthday / 100;
		// ����ȡ����
		int day = birthday % 100;
		// ����
		String xingZuo = "";
		
		// �ж�����
		switch (month) {
		case 1:
			// ��Ԫ���� OperationalCharacter.java 
			xingZuo = day > 20 ? "ˮƿ��":"Ħ����";
			break;
		case 2:
			xingZuo = day > 19 ? "˫����":"ˮƿ��";
			break;
		case 3:
			xingZuo = day > 20 ? "������":"˫����";
			break;
		case 4:
			xingZuo = day > 20 ? "��ţ��":"������";
			break;
		case 5:
			xingZuo = day > 21 ? "˫����":"��ţ��";
			break;
		case 6:
			xingZuo = day > 21 ? "��з��":"˫����";
			break;
		case 7:
			xingZuo = day > 22 ? "ʨ����":"��з��";
			break;
		case 8:
			xingZuo = day > 23 ? "��Ů��":"ʨ����";
			break;
		case 9:
			xingZuo = day > 23 ? "������":"��Ů��";
			break;
		case 10:
			xingZuo = day > 23 ? "��Ы��":"������";
			break;
		case 11:
			xingZuo = day > 22 ? "������":"��Ы��";
			break;
		case 12:
			xingZuo = day > 21 ? "Ħ����":"������";
			break;
		default:
			System.out.println("�������ո�ʽ���󣡣���");
			break;
		}
		
		System.out.println("���������ǣ�"+xingZuo);
		
		input.close();
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo();
	}

}
