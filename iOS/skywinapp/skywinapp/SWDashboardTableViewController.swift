//
//  SWDashboardTableViewController.swift
//  skywinapp
//
//  Created by Matteo on 28/05/16.
//  Copyright © 2016 Matteo. All rights reserved.
//

import UIKit
import SwiftyJSON

class SWDashboardTableViewController: UITableViewController {
    @IBOutlet weak var homeScore: UILabel!
    @IBOutlet weak var homeTeam: UILabel!
    @IBOutlet weak var guestScore: UILabel!
    @IBOutlet weak var guestTeam: UILabel!
    
    var homeplayers: JSON!
    var guestplayers: JSON!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        self.homeScore.layer.cornerRadius = self.homeScore.frame.size.width / 2;
        self.homeScore.layer.masksToBounds = true
        self.guestScore.layer.cornerRadius = self.guestScore.frame.size.width / 2;
        self.guestScore.layer.masksToBounds = true

        
        // Uncomment the following line to preserve selection between presentations
        // self.clearsSelectionOnViewWillAppear = false

        // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
        // self.navigationItem.rightBarButtonItem = self.editButtonItem()
        
        refreshValues()
        NSTimer.scheduledTimerWithTimeInterval(1, target: self, selector: #selector(SWDashboardTableViewController.refreshValues), userInfo: nil, repeats: true)

        
    }
    //1960aa
    func refreshValues(){
        SWEngine.sharedInstance.getDashboard({(description) in
            
            self.guestScore.text = String(format: "%d" ,description["guest_score"].int!)
            self.guestTeam.text = description["guest_team"]["name"].string
            self.homeScore.text = String(format: "%d" ,description["home_score"].int!)
            self.homeTeam.text = description["home_team"]["name"].string
            
            self.homeplayers = description["home_team"]["players"]
            self.guestplayers = description["guest_team"]["players"]
            dispatch_async(dispatch_get_main_queue(), {

            self.tableView.reloadData()
                
            })
            
            }, failureBlock: {(error) in })
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    // MARK: - Table view data source

    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        // #warning Incomplete implementation, return the number of sections
        return 2
    }
    
    override func tableView(tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        
        switch section {
        case 0:
            return self.homeTeam.text
        case 1:
            return self.guestTeam.text
        default:
            return self.guestTeam.text
        }
    }

    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        switch section {
        case 0:

            if self.homeplayers != nil {
                return (self.homeplayers.array?.count)!
            }
            return 0
        case 1:
            
            if self.guestplayers != nil {
                return (self.guestplayers.array?.count)!
            }
                
            return 0
        default:
            return 0
        }
    }

    
    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCellWithIdentifier("SWPlayerCell", forIndexPath: indexPath) as! SWPlayerCell
        var res : String!
        var imagename: String!
        var tally: String!

        switch indexPath.section {
        case 0:
            res = String(format: "%@ %@ - %d",  homeplayers[indexPath.row]["first_name"].string!,  homeplayers[indexPath.row]["second_name"].string!, homeplayers[indexPath.row]["tally"].int!)
            imagename = String(format: "%@.jpg", homeplayers[indexPath.row]["second_name"].string!)
            tally = String(format: "%d", homeplayers[indexPath.row]["tally"].int!)

            
        case 1:
            res = String(format: "%@ %@ - %d",  guestplayers[indexPath.row]["first_name"].string!,  guestplayers[indexPath.row]["second_name"].string!, guestplayers[indexPath.row]["tally"].int!)
            imagename = String(format: "%@.jpg", guestplayers[indexPath.row]["second_name"].string!)
            tally = String(format: "%d", guestplayers[indexPath.row]["tally"].int!)
        default:
            res = "home"
        }
        
        cell.playerName?.text = res
        cell.playerimage.image = UIImage(named: imagename)
        cell.tally.text = tally
        cell.backgroundColor = SWEngine.sharedInstance.hexStringToUIColor("#1960aa")

        // Configure the cell...

        return cell
    }
    

    /*
    // Override to support conditional editing of the table view.
    override func tableView(tableView: UITableView, canEditRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return false if you do not want the specified item to be editable.
        return true
    }
    */

    /*
    // Override to support editing the table view.
    override func tableView(tableView: UITableView, commitEditingStyle editingStyle: UITableViewCellEditingStyle, forRowAtIndexPath indexPath: NSIndexPath) {
        if editingStyle == .Delete {
            // Delete the row from the data source
            tableView.deleteRowsAtIndexPaths([indexPath], withRowAnimation: .Fade)
        } else if editingStyle == .Insert {
            // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
        }    
    }
    */

    /*
    // Override to support rearranging the table view.
    override func tableView(tableView: UITableView, moveRowAtIndexPath fromIndexPath: NSIndexPath, toIndexPath: NSIndexPath) {

    }
    */

    /*
    // Override to support conditional rearranging of the table view.
    override func tableView(tableView: UITableView, canMoveRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return false if you do not want the item to be re-orderable.
        return true
    }
    */

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */


}
