---
title: "Create and Modify Cavity Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Modify_Cavity_Feature_Example_VB.htm"
---

# Create and Modify Cavity Feature Example (VBA)

This example shows how to create and modify a cavity feature.

```
'-----------------------------------------------------------------------------------------------
' Preconditions:
' 1. Create a new folder and copy public_documents\samples\tutorial\molds\telephone.sldprt to that
'    folder.
' 2. Click File > New > Part and OK to create a new part document.
'    a. Insert a sketch of a rectangle with a length of 240 mm and width of 350 mm.
'    b. Using the sketch, create a boss extrude feature with a depth of 160 mm.
'    c. Save the part as telephoneMoldBase.sldprt in the folder created in step 1.
' 3. Click File > New > Assembly and OK to create a new assembly document.
'    a. Click telephoneMoldBase in Part/Assembly to Insert in the PropertyManager page.
'    b. Click OK.
'    c. Click Insert Components on the Assembly toolbar, click Browse in
'       Part/Assembly to Insert, click telephone.sldprt located in the folder created in step 1,
'       and click Open.
'    d. Drop telephone.sldprt in the graphics area.
'    e. Click View > Display > Hidden Lines Visible.
'    f. In the FeatureManager design tree, click telephone<1> and click Move Component
'       in the Assembly toolbar.
'    g. Move telephone<1> into the center of telephoneMoldBase<1> and click OK.
'    h. Click File > Save All > Rebuild and save the document (recommended), navigate to the
'       folder created in step 1, type AssemInterim.sldasm in File name, and click Save.
'    i. In the FeatureManager design tree, click telephoneMoldBase<1> and click Edit Component
'       in the Assembly toolbar.
'    j. Click Cavity on the Mold Tools toolbar.
'    k. Click telephone<1> in the FeatureManager design tree for the design component.
'    l. Clear Scale uniformly and set X, Y, and Z to 0, if necessary.
'    m. Click OK to create the cavity feature and close the PropertyManager page.
' 4. Click File > Save All.
' 5. Click File > Close two times.
' 6. Click File > AssemInterim.sldasm.
' 7. Open the Immediate window.
' 8. Run the macro.
'
' Postconditions:
' 1. Accesses Cavity<1> and gets and sets scale-related properties.
' 2. When the macro finishes executing, click File > Close and Save All.
' 3. Open AssemInterim.sldasm, click Yes to roll forward, and click Rebuild to rebuild.
' 4. Expand telephoneMoldBase<1> in the FeatureManager design tree.
' 5. Right-click the Cavity1 feature, click Edit Feature, click OK if a message box displays, and
'    compare the values in the PropertyManager page with the new values shown in the
'    Immediate window.
' 6. Click OK.
' 7. Close File > Close > Save All.
'-----------------------------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swFeature As SldWorks.Feature
Dim swCavityFeatureData As SldWorks.CavityFeatureData
Dim status As Boolean
Dim xScale As Double
Dim yScale As Double
Dim zScale As Double
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
```

```
    'Select the Cavity1 feature and get and set its properties
    status = swModelDocExt.SelectByID2("Cavity1@telephoneMoldBase-1@AssemInterim", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swCavityFeatureData = swFeature.GetDefinition
    status = swCavityFeatureData.AccessSelections(swModel, Nothing)
        Debug.Print ("Scale type: " & swCavityFeatureData.ScaleType)
        Debug.Print ("Scale uniformly value: " & swCavityFeatureData.UseUniformScale)
        swCavityFeatureData.GetScale xScale, yScale, zScale
        Debug.Print ("Scale values:")
        Debug.Print ("  X: " & xScale)
        Debug.Print ("  Y: " & yScale)
        Debug.Print ("  Z: " & zScale)
        Debug.Print ("Value by which to scale this cavity feature in all directions: " & swCavityFeatureData.UniformScale)
        Debug.Print ("")
        swCavityFeatureData.UseUniformScale = True
        Debug.Print ("New scale uniformly value: " & swCavityFeatureData.UseUniformScale)
        swCavityFeatureData.UniformScale = 2
        Debug.Print ("New value by which to scale this cavity feature in all directions: " & swCavityFeatureData.UniformScale)
        status = swFeature.ModifyDefinition(swCavityFeatureData, swModel, Nothing)
```

```
End Sub
```
