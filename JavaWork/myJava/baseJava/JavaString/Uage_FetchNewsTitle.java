/**
* Filename : Uage_FetchNewsTitle.java
* Author : DengPengFei
* Creation time : ����5:38:38 - 2020��5��9��
*/
package JavaString;

/*
 * 	Java��ȡ���ű���
 */

public class Uage_FetchNewsTitle {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		demo1();
		
	}
	
	public static void demo1() {
		
		/*
		 * ��������վ��ͨ�����б����ʽ��ʾ�������ŵĶ�̬���⡣
		 * һ������£�һ����ʾһ�����ű��⣬�����ű��������Ƚϳ��������Ҫ�������н�ȡ��������������ʾ��һ��ʡ�Ժš�����
		 */
		
		String[] news = {"��ο�������Java", "����������Java�е������", "ѧϰJava��ʮ���Ҹ�", "������֪����java�����̼��ɴ�ȫ", "Java�������ȫ"};
		
		/*
	     * ѭ�����������ȡ����Ԫ���е�ǰ10���ַ���Ϊ�б�չʾ
	     */
		System.out.println("************* �����б� *************");
		
		for (String title : news) {
			
			int titleLenght = title.length();
			
			if (titleLenght > 10 ) {
				System.out.println(title.substring(0,10)+"...");
			}else {
				System.out.println(title);
			}
			
		}
		
	}

}
