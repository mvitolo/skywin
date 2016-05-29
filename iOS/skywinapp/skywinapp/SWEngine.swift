//
//  SWEngine.swift
//  skywinapp
//
//  Created by Matteo on 28/05/16.
//  Copyright © 2016 Matteo. All rights reserved.
//

import Foundation
import SwiftyJSON

class SWEngine: NSObject {
    
    var newCookie : NSHTTPCookie!
    static let sharedInstance: SWEngine = SWEngine()
    
    var numberofvotes : Int!
    
    
    
    func makePOSTRequest(urlstring: String, successBlock: (dictionary: JSON) -> Void, failureBlock:(error: NSError?) -> Void){
        
        let request = NSMutableURLRequest(URL: NSURL(string: urlstring)!)
        request.HTTPMethod = "GET"
        
        let session = NSURLSession.sharedSession()
        
        let task = session.dataTaskWithRequest(request) { data, response, error in
            // make sure there wasn't a fundamental networking error
            
            guard error == nil && data != nil else {
                print(error)
                return
            }
            
            // if you're going to check for NSHTTPURLResponse, then do something useful
            // with it, e.g. see if server status code indicates that everything is OK
            
            if let httpResponse = response as? NSHTTPURLResponse {
                if httpResponse.statusCode != 200 {
                    print("statusCode != \(httpResponse.statusCode)")
                }
            }
            
            // since you set `Accept` to JSON, I'd assume you'd want to parse it:
            
            let responseObject = JSON(data: data!)
            print(responseObject)
            if responseObject["status"]  != "NOK_SESS" && responseObject["status"]  != "KO" {
                
                successBlock(dictionary: responseObject)
            } else {
                if responseObject["status"]  == "KO" {
                    
                    failureBlock(error: error)
                    return
                }
            }
            
            
        }
        task.resume()
    }
    

    
    
    func getDashboard( successBlock: (dictionary: JSON)-> Void, failureBlock: (error: NSError?)-> Void) {
        
        makePOSTRequest("https://skywin.herokuapp.com/api/matches/1/?format=json", successBlock: successBlock, failureBlock: failureBlock)
       /*
        if let path = NSBundle.mainBundle().pathForResource("results", ofType: "json") {
            do {
                let data = try NSData(contentsOfURL: NSURL(fileURLWithPath: path), options: NSDataReadingOptions.DataReadingMappedIfSafe)
                let jsonObj = JSON(data: data)
                if jsonObj != JSON.null {
                    successBlock(dictionary: jsonObj)
                } else {
                    print("could not get json from file, make sure that file contains valid json.")
                }
            } catch let error as NSError {
                print(error.localizedDescription)
            }
        } else {
            print("Invalid filename/path.")
        }*/

        
    }
    
    func hexStringToUIColor (hex:String) -> UIColor {
        var cString:String = hex.stringByTrimmingCharactersInSet(NSCharacterSet.whitespaceAndNewlineCharacterSet() as NSCharacterSet).uppercaseString
        
        if (cString.hasPrefix("#")) {
            cString = cString.substringFromIndex(cString.startIndex.advancedBy(1))
        }
        
        if ((cString.characters.count) != 6) {
            return UIColor.grayColor()
        }
        
        var rgbValue:UInt32 = 0
        NSScanner(string: cString).scanHexInt(&rgbValue)
        
        return UIColor(
            red: CGFloat((rgbValue & 0xFF0000) >> 16) / 255.0,
            green: CGFloat((rgbValue & 0x00FF00) >> 8) / 255.0,
            blue: CGFloat(rgbValue & 0x0000FF) / 255.0,
            alpha: CGFloat(1.0)
        )
    }

}