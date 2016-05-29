//
//  SWLeaderboardCell.swift
//  skywinapp
//
//  Created by Matteo on 29/05/16.
//  Copyright © 2016 Matteo. All rights reserved.
//

import UIKit

class SWLeaderboardCell: UITableViewCell {

    @IBOutlet weak var playerImage: UIImageView!
   
    @IBOutlet weak var playerName: UILabel!
    
    @IBOutlet weak var playerpoints: UILabel!
    
    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }

    override func setSelected(selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }

}
