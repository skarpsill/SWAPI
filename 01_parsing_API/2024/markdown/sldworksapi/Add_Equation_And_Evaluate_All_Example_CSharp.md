---
title: "Add Equation and Evaluate All Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Equation_And_Evaluate_All_Example_CSharp.htm"
---

# Add Equation and Evaluate All Example (C#)

This example shows how to use EquationMgr interfaces to add an equation
to a model and

delay evaluation until all equations have been added.

```
//------------------------------------------------------------------------
// Preconditions:
// 1. Open any model document.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Rebuild the model.
// 2. Observe the 26 (A-Z) new equations in the Equations folder in the
//    FeatureManager design tree.
// 3. Observe the near-zero evaluation time for each equation in the
//    Immediate Window, demonstrating that the evaluations were delayed.
//------------------------------------------------------------------------
```

using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swconst;

using System;

using System.Diagnostics;

namespace AddEquationAndEvaluateAll_CSharp.csproj

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}partial
class SolidWorksMacro

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
void Main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ModelDoc2
swModel = default(ModelDoc2);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel
= (ModelDoc2)swApp.**ActiveDoc**;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}EquationMgr
MyEqu = default(EquationMgr);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}int
Index = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}long
lValue = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}long
evalStatus = 0;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}System.DateTime
t1 = default(System.DateTime);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}System.DateTime
t2 = default(System.DateTime);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}long
i = 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}i
= 0;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MyEqu
= swModel.**GetEquationMgr**();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}if
(MyEqu.**GetCount**() > 0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}while
((i < 26))

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MyEqu.**Delete**(0);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}i
= i + 1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Delaying
evaluation of equations until the end...");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(Index = System.Convert.ToInt32('A'); Index <= System.Convert.ToInt32('Z');
Index++)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}t1
= DateTime.Now;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//Delay
solving each equation until after all equations are added
//(set solve parameter
to false)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//FeatureManager
design tree not updated

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}lValue
= MyEqu.Add2(Index, "\""
+ System.Convert.ToChar(Index) + "\"=" + Index, false);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}t2
= DateTime.Now;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Time
of evaluation for character " + System.Convert.ToChar(Index) + ":
");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}TimeSpan
t3 = t2 - t1;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(t3.ToString());

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Number
of equations added to EquationMgr is " + MyEqu.**GetCount**());

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//Solve
all equations after they have been added
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//FeatureManager
design tree updated

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Evaluating
all equations...");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}evalStatus
= MyEqu.EvaluateAll();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Finished
Add2 and EvaluateAll");

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MyEqu
= null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel
= null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//swApp.**CloseAllDocuments**True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp
= null;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
SldWorks swApp;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

}
