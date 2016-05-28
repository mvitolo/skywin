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
    
    func getDashboard( successBlock: (dictionary: JSON)-> Void, failureBlock: (error: NSError?)-> Void) {
        
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
        }

        
    }

}