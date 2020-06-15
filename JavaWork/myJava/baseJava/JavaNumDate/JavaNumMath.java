/**
* Filename : JavaNumMath.java
* Author : DengPengFei
* Creation time : ����4:52:18 - 2020��5��21��
*/
package JavaNumDate;

/*
 * �� Java �� Math ���װ�˳��õ���ѧ���㣬�ṩ�˻�������ѧ��������ָ����������ƽ���������Ǻ����ȡ�
 * Math ��λ�� java.lang �������Ĺ��췽���� private �ģ�����޷����� Math ��Ķ��󣬲��� Math ���е����з��������෽��������ֱ��ͨ����������������
 */

public class JavaNumMath {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo1();
		demo2();
		
	}

	public static void demo1() {
		
		/*
		 * Math ���а��� E �� PI ������̬����������������������ʾ�ģ����ǵ�ֵ�ֱ���� e����Ȼ�������� �У�Բ���ʣ�
		 */
		
		System.out.println("E ������ֵ��" + Math.E);
		System.out.println("PI ������ֵ��" + Math.PI);
		
	}
	
	// �����ֵ����Сֵ�;���ֵ
	public static void demo2() {
		
		System.out.println("�����ֵ��" + Math.max(20, 21));
		System.out.println("����Сֵ��" + Math.min(20, 21));
		System.out.println("�����ֵ��" + Math.abs(-21));
		
	}
	
}
