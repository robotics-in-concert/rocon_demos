package kr.co.smartylab.CafeRemoteOrderApp;

import android.app.Activity;
import android.content.res.AssetManager;
import android.location.Location;
import android.location.LocationListener;
import android.os.Bundle;
import android.webkit.GeolocationPermissions;
import android.webkit.JavascriptInterface;
import android.webkit.WebChromeClient;
import android.webkit.WebView;

import java.io.IOException;
import java.io.InputStream;

public class MyActivity extends Activity {
    class LocationProvider implements LocationListener {
        private WebView webView;

        public LocationProvider(WebView webView) {
            this.webView = webView;
        }

        @JavascriptInterface
        public String getLocation() {
            return "lastLocation";
        }

        @Override
        public void onLocationChanged(Location location) {
            lastLocation = location;
            webView.loadUrl("javascript:updateLocation('args')");
        }

        @Override
        public void onStatusChanged(String s, int i, Bundle bundle) {

        }

        @Override
        public void onProviderEnabled(String s) {

        }

        @Override
        public void onProviderDisabled(String s) {

        }

    }

    private Location lastLocation;
    private WebView webView;
    private LocationProvider locationProvider;

    /**
     * Called when the activity is first created.
     */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);

        // Init attrs
        webView = (WebView) findViewById(R.id.webView);
        locationProvider = new LocationProvider(webView);

        // Prepare web view
        webView.getSettings().setJavaScriptEnabled(true);
        webView.addJavascriptInterface(locationProvider, "LocationProvider");

        AssetManager assetManager = getAssets();
        String htmlPage = null;
        InputStream input;
        try {
            input = assetManager.open("web/index.html");

            int size = input.available();
            byte[] buffer = new byte[size];
            input.read(buffer);
            input.close();
            // byte buffer into a string
            htmlPage = new String(buffer);

        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        webView.setWebChromeClient(new WebChromeClient() {
            @Override
            public void onGeolocationPermissionsShowPrompt(String origin, GeolocationPermissions.Callback callback) {
                callback.invoke(origin, true, false);
            }
        });
        webView.loadDataWithBaseURL("file:///android_asset/", htmlPage, "text/html", "utf-8", "");

        // Register location listener
        //LocationManager lm = (LocationManager) getSystemService(LOCATION_SERVICE);
        //lm.requestLocationUpdates(LocationManager.GPS_PROVIDER, 0, 0, locationProvider);
    }

}
