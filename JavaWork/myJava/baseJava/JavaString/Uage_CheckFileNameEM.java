/**
* Filename : Uage_CheckFileNameEM.java
* Author : DengPengFei
* Creation time : ����9:21:35 - 2020��5��11��
*/
package JavaString;
import java.util.Scanner;

public class Uage_CheckFileNameEM {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo1();
		
	}
	
	public static void demo1() {
		
		/*
		 * ���裬����ҵ�ύϵͳ��ѧ����Ҫ¼���ύ�� Java �ļ����Ƽ�Ҫ�ύ���������ַ��
		 * ��ô����Ҫ��ѧ���������Щ��Ϣ����У�飬�ж������Ƿ�����
		 * У��Ĺ���Ϊ��¼����ļ����Ʊ����ԡ�.java����β��¼��������ַ�б�������С�@�����ź͡�.�����ţ��ҡ�@���ڡ�.��֮ǰ��
		 * 
		 */
		
		Scanner input = new Scanner(System.in);
		System.out.println("********** ����ӭ��¼��ҵ�ύϵͳ�� **********");
		// �����ļ�����
		System.out.println("��������ҵ���ƣ�");
		// ��ȡ������Ϣ
		String name = input.next();
		// ���������ַ
		System.out.println("�����������ַ��");
		// ��ȡ������Ϣ
		String email = input.next();
		
		// ��������ļ����������ַ
		boolean nameCon = false;
		boolean emailCon = false;
		
		// ��ȡ�ļ����� . ������ֵ
		int index = name.indexOf(".java");
		// �ж��ļ�����  *** �����ַ�Ҫʹ�õ�����
		if (index != -1) {
			if (name.charAt(index+1) == 'j' && name.charAt(index+2) == 'a' && 
					name.charAt(index+3) == 'v' && name.charAt(index+4) == 'a') {
				nameCon = true;
			}
		}else {
			nameCon = false;
		}
		// �ж������ַ
		int index1 = email.indexOf('@');
		int index2 = email.indexOf('.');
		if (index1 != -1 && index2 != -1 && index1 < index2) {
			emailCon = true;
		}else {
			emailCon = false;
		}
		// �ж��Ƿ��ύ�ɹ�
		if (nameCon && emailCon) {
			System.out.println("��ҵ�ύ�ɹ���");
		}else {
			if (nameCon) {
				System.out.println("�����ַ��ʽ����");
			}else if (emailCon) {
				System.out.println("�ļ����Ƹ�ʽ����");
			}else {
				System.out.println("�ļ����ƻ������ַ��ʽ����");
			}
		}
		input.close();
		
	}

}
