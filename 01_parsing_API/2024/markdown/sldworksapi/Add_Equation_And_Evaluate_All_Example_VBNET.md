---
title: "Add Equation and Evaluate All Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Equation_And_Evaluate_All_Example_VBNET.htm"
---

# Add Equation and Evaluate All Example (VB.NET)

This example shows how to use IEquationMgr interfaces
to add an equation to a model and delay evaluation until all equations are added.

```
'------------------------------------------------------------------------
' Preconditions:
' 1. Open any model document.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Rebuild the model.
' 2. Observe the 26 (A-Z) new equations in the Equations folder in the
'    FeatureManager design tree.
' 3. Observe the near-zero evaluation time for each equation in the
'    Immediate Window, demonstrating that the evaluations were delayed.
'------------------------------------------------------------------------
#Const ccTIMER = 1
```

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Public
Sub Main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModel As ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel
= swApp.**ActiveDoc**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
MyEqu As EquationMgr

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Index As Integer

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
lValue As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
evalStatus As Long

#If ccTIMER = 1 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
t1 As Single

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
t2 As Single

#Else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
t1kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Date

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
t2kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Date

#End If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
i As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}i
= 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MyEqu
= swModel.**GetEquationMgr**

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
MyEqu.**GetCount**> 0 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Do
While (i < 26)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MyEqu.**Delete**(0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}i
= i + 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Loop

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Delaying
evaluation of equations until the end...")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
Index = Asc("A") To Asc("Z")

#If ccTIMER = 1 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}t1
= Timer

#Else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}t1
= Now

#End If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Delay
solving each equation until after all equations are
'added (set solve parameter
to false)
kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'FeatureManager
design tree not updated

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}lValue
= MyEqu.Add2(Index, """"
& Microsoft.VisualBasic.Chr(Index) & """="
& Index, False)

#If ccTIMER = 1 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}t2
= Timer

#Else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}t2
= Now

#End If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Time
of evaluation for character " + Microsoft.VisualBasic.Chr(Index)
+ ": ")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print(t2
- t1)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
Index

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Number
of equations added to EquationMgr is " & MyEqu.**GetCount**)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Solve
all equations after they have been added
kadov_tag{{</spaces>}}'FeatureManager
design tree updated

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Evaluating
all equations...")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}evalStatus
= MyEqu.EvaluateAll()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print("Finished
Add2 and EvaluateAll")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}MyEqu
= Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel
= Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'swApp.**CloseAllDocuments**True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp
= Nothing

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Public
swApp As SldWorks

End Class
