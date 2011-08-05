package com.pipetree.joseph.test.yrs.ndmisbn;


import java.net.*;
import java.io.*;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;
import android.widget.TextView;
import com.pipetree.joseph.test.yrs.ndmisbn.Global;

public class main extends Activity {

	/** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        
        Button barbutton = (Button)findViewById(R.id.barscan);
        barbutton.setOnClickListener(barScan);
        
        Button qrbutton = (Button)findViewById(R.id.qrscan);
        qrbutton.setOnClickListener(qrScan);
        
        Button sendbutton = (Button)findViewById(R.id.sendData);
        sendbutton.setOnClickListener(sendData);
        
        Button resetbutton = (Button)findViewById(R.id.reset);
        resetbutton.setEnabled(false);
        resetbutton.setOnClickListener(reset);
        
        Global.isbnTextView = (TextView)findViewById(R.id.ISBNLabel);
        Global.thingIDTextView = (TextView)findViewById(R.id.ThingIDLabel);
        
        Global.update();
        
        
    }
    

    
    public static String getThingID(String url){
    	
    	String[] temp;
    	
    	String delimeter = "thing/";
    	
    	temp = url.split(delimeter);
    	
		return temp[1];
    	
    }
    
    public static String sendGetRequest(String endpoint, String requestParameters)
    {
    String result = null;
    if (endpoint.startsWith("http://"))
    {
    // Send a GET request to the servlet
    try
    {
    // Send data
    String urlStr = endpoint;
    if (requestParameters != null && requestParameters.length () > 0)
    {
    urlStr += "?" + requestParameters;
    }
    URL url = new URL(urlStr);
    URLConnection conn = url.openConnection ();
    // Get the response
    BufferedReader rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
    StringBuffer sb = new StringBuffer();
    String line;
    while ((line = rd.readLine()) != null)
    {
    sb.append(line);
    }
    rd.close();
    result = sb.toString();
    } catch (Exception e)
    {
    e.printStackTrace();
    }
    }
    return result;
    }
    
    public void doRequest() {
    	
    	final String TAG = "MAIN";
    	
    	String url = Global.DOMAIN.concat("isbn");
    	String param1 = Global.isbn;
    	String param2 = Global.thingid;
    	
    	String params1 = "isbn=".concat(param1);
    	String params2 = "&thingid=".concat(param2);
    	String params3 = params1.concat(params2);
    	
    	Log.v(TAG, "param1=" + param1);
    	Log.v(TAG, "param2=" + param2);
    	
    	Log.v(TAG, "params1=" + params1);
    	Log.v(TAG, "params2=" + params2);
    	Log.v(TAG, "params3=" + params3);
    	
    	//params3 = "isbn=9780596002022&thingid=oaHYyC93eV2rPwMJCnG5";
    	
    	Context context = getApplicationContext();
		CharSequence text = params3;
		int duration = Toast.LENGTH_LONG;

		Toast toast = Toast.makeText(context, text, duration);
		toast.show();
    	
    	String res = sendGetRequest(url, params3);
    	
     
    }
    
    public Button.OnClickListener barScan = new Button.OnClickListener() {
        public void onClick(View v) {
            Intent intent = new Intent("com.google.zxing.client.android.SCAN");
            intent.putExtra("SCAN_MODE", "BARCODE_MODE");
            startActivityForResult(intent, 0);
        }
    };
    
    public Button.OnClickListener qrScan = new Button.OnClickListener() {
        public void onClick(View v) {
        	
        	if (Global.isbn != ""){
        		Intent intent = new Intent("com.google.zxing.client.android.SCAN");
                intent.putExtra("SCAN_MODE", "QR_CODE_MODE");
                startActivityForResult(intent, 1);
        	} else {
        		Context context = getApplicationContext();
        		CharSequence text = "You need to scan a Barcode first!";
        		int duration = Toast.LENGTH_LONG;

        		Toast toast = Toast.makeText(context, text, duration);
        		toast.show();
        	}
        	
        }
    };
    
    public Button.OnClickListener reset = new Button.OnClickListener() {
        public void onClick(View v) {
            Global.isbn = "";
            Global.thingid = "";
            Global.update();
        }
    };
    
    public Button.OnClickListener sendData = new Button.OnClickListener() {
        public void onClick(View v) {
         
        	if(Global.thingid != ""){
				doRequest();
				Global.isbn = "";
				Global.thingid = "";
				Global.update();
        	} else {
        		Context context = getApplicationContext();
        		CharSequence text = "You need to scan more Data first!";
        		int duration = Toast.LENGTH_LONG;

        		Toast toast = Toast.makeText(context, text, duration);
        		toast.show();
        	}
        }
    };
    
    
    public void onActivityResult(int requestCode, int resultCode, Intent intent) {
        if (requestCode == 0) {
            if (resultCode == RESULT_OK) {
                String contents = intent.getStringExtra("SCAN_RESULT");
                String format = intent.getStringExtra("SCAN_RESULT_FORMAT");
                // Handle successful scan
                
                
                Global.isbn = contents;
                Global.update();
                
                	                	
            } else if (resultCode == RESULT_CANCELED) {
                // Handle cancel
            }
        }
        
        if (requestCode == 1) {
            if (resultCode == RESULT_OK) {
                String contents = intent.getStringExtra("SCAN_RESULT");
                String format = intent.getStringExtra("SCAN_RESULT_FORMAT");
                // Handle successful scan
                
                String t;
                
                t = getThingID(contents);
                
                Global.thingid = t;
                Log.v("MAIN", "thingid =" + t);
                Global.update();
                	
                	                	
            } else if (resultCode == RESULT_CANCELED) {
                // Handle cancel
            }
        }
        
        
    }
    
    
    
    
}