//
//  ViewController.swift
//  01-build_model_via_coremltools
//
//  Created by Marlon Leng on 2018/6/9.
//  Copyright © 2018年 Marlon Leng. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
//        使用模型
        let model = HousePricer.init()
        let output = try! model.prediction(RM: 6.5, LSTAT: 5, PTRATIO: 19)
        print("housePredictPrice = \(output.MEDV)")
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

