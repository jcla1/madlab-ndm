package com.pipetree.joseph.test.yrs.ndmisbn;

import android.widget.TextView;

public class Global {
	public static String isbn = "";
    public static String thingid = "";
    
    public static TextView isbnTextView;
    public static TextView thingIDTextView;
    
    public static String DOMAIN = "http://madlab-ndm.appspot.com/";
    
    public static void update(){
    	
        isbnTextView.setText(isbn);
        
        thingIDTextView.setText(thingid);
    }
    
}