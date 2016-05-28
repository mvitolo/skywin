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
    
    var players: JSON!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        self.homeScore.layer.cornerRadius = self.homeScore.frame.size.width / 2;
        self.guestScore.layer.cornerRadius = self.guestScore.frame.size.width / 2;

        
        // Uncomment the following line to preserve selection between presentations
        // self.clearsSelectionOnViewWillAppear = false

        // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
        // self.navigationItem.rightBarButtonItem = self.editButtonItem()
        
        refreshValues()
        NSTimer.scheduledTimerWithTimeInterval(1, target: self, selector: #selector(SWDashboardTableViewController.refreshValues), userInfo: nil, repeats: true)

        
    }
    
    func refreshValues(){
        SWEngine.sharedInstance.getDashboard({(description) in
            
            self.guestScore.text = String(format: "%d" ,description["guestScore"].int!)
            self.guestTeam.text = description["guestTeam"].string
            self.homeScore.text = String(format: "%d" ,description["homeScore"].int!)
            self.homeTeam.text = description["homeTeam"].string
            
            self.players = description["players"]
            
            self.tableView.reloadData()
            
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
            return (players["home"].array?.count)!
        case 1:
            return (players["guest"].array?.count)!
        default:
            return 0
        }
    }

    
    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCellWithIdentifier("SWPlayerCell", forIndexPath: indexPath)
        var team : String!
        switch indexPath.section {
        case 0:
            team = "home"
        case 1:
            team = "guest"
        default:
            team = "home"
        }
        let res = String(format: "%@ %@ - %d",  players[team][indexPath.row]["firstName"].string!,  players[team][indexPath.row]["secondName"].string!, players[team][indexPath.row]["tally"].int!)
        
        cell.textLabel?.text = res

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
