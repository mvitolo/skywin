//
//  SWPlayCell.swift
//  skywinapp
//
//  Created by Matteo on 29/05/16.
//  Copyright © 2016 Matteo. All rights reserved.
//

import UIKit
import QuartzCore


class SWPlayerCell: UITableViewCell {

    
    @IBOutlet weak var tally: UILabel!
    @IBOutlet weak var playerimage: UIImageView!
    
    @IBOutlet weak var playerName: UILabel!
    
    override func awakeFromNib() {
        super.awakeFromNib()
        
        playerimage.layer.cornerRadius = playerimage.frame.size.width/2
        tally.layer.cornerRadius = tally.frame.size.width/2
        tally.layer.masksToBounds = true

        // Initialization code
    }

    override func setSelected(selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }

}
