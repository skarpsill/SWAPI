---
title: "Activate Smart Feature in an Assembly Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Activate_Smart_Features_in_an_Assembly_Example_CSharp.htm"
---

# Activate Smart Feature in an Assembly Example (C#)

This example shows how to activate a Smart Feature in an assembly.

```
//----------------------------------------------------------------------------
// Preconditions: Open public_documents\samples\tutorial\api\testSmartAssembly.sldasm.
//
// Postconditions:
// 1. Activates Smart Feature holecube-1 and creates two extruded cuts
//    for the selected reference entity.
// 2. Displays Smart Feature holecube-1 in the FeatureManager design tree.
// 3. Creates Smart-Feature1 in component testpart100.
// 4. Expand and examine testpart100 and holecube-1 in the FeatureManager
//    design tree.
//
// NOTE: Because the model is used elsewhere, do not save changes.
//---------------------------------------------------------------------------

	using Microsoft.VisualBasic;

	using System;

	using System.Collections;

	using System.Collections.Generic;

	using System.Data;

	using System.Diagnostics;

	using SolidWorks.Interop.sldworks;

	using SolidWorks.Interop.swconst;

	using System.Runtime.InteropServices;

	namespace ActivateSmartFeature_CSharp.csproj

	{

	    partial class SolidWorksMacro

	    {

	        Component2 comp;

	        object comps;

	        Object[] compsArray;

	        SelectionMgr selMgr;

	        object features;

	        object featuresSelected;

	        Boolean[] featuresSelectedArray;

	        object components;

	        object componentsSelected;

	        Boolean[] componentsSelectedArray;

	        object references;

	        Object[] referenceArray;

	        Face2 face;

	        AssemblyDoc swAss;

	        ModelDoc2 doc;

	        bool boolstatus;

	        int i;

	        int j;

	        public void Main()

	        {

	            swAss = (AssemblyDoc)swApp.ActiveDoc;

	            comps = swAss.GetComponents(true);

	            compsArray = (Object[])comps;

	            doc = (ModelDoc2)swAss;

	            selMgr = (SelectionMgr)doc.SelectionManager;

	            for (i = 0; i <= compsArray.GetUpperBound(0); i++)

	            {

	                comp = (Component2)compsArray[i];

	                if (comp.IsSmartComponent())

	                {

	                    if (comp.GetSmartComponentData(out features, out featuresSelected, out components, out componentsSelected, out references))

	                    {

	                        if ((featuresSelected == null)
	== false)

	                        {

	                            featuresSelectedArray = (Boolean[])featuresSelected;

	                            for (j = 0; j <= featuresSelectedArray.GetUpperBound(0); j++)

	                            {

	                                if (featuresSelectedArray[j] == false)

	                                {

	                                    featuresSelectedArray[j] = true;

	                                }

	                            }

	                        }

	                        if ((componentsSelected == null)
	== false)

	                        {

	                            componentsSelectedArray = (Boolean[])componentsSelected;

	                            for (j = 0; j <= componentsSelectedArray.GetUpperBound(0); j++)

	                            {

	                                if (componentsSelectedArray[j] == false)

	                                {

	                                    componentsSelectedArray[j - 1] = true;

	                                }

	                            }

	                        }

	                        boolstatus = doc.Extension.SelectByID2("", "FACE",
	-0.1054255613309, -0.008376708432593, 0.03086069829328, false, 0, null, 0);

	                        face = (Face2)selMgr.GetSelectedObject6(1,
	-1);

	                        referenceArray = (Object[])references;

	                        referenceArray[0] = face;

	                        DispatchWrapper[] arrRefsIn = new DispatchWrapper[1];

	                        arrRefsIn[0] = new DispatchWrapper(referenceArray[0]);

	                        boolstatus = comp.SetSmartComponentData(featuresSelected, componentsSelected, (arrRefsIn));

	                    }

	                    Debug.Print(comp.Name);

	                }

	            }

	        }

	        public SldWorks swApp;

	    }

	}
```
