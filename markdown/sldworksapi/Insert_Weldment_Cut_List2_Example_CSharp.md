---
title: "Insert Weldment Cut List Example #2 (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Weldment_Cut_List2_Example_CSharp.htm"
---

# Insert Weldment Cut List Example #2 (C#)

This example shows how to insert a weldment cut list into the FeatureManager
design tree.

```
//----------------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\assemblymates\bracket.sldprt.
// 2. Click Tools > Options > System Options > FeatureManager >
//    Solid Bodies > Show > OK.
// 3. Expand the Solid Bodies(1) folder in the FeatureManager design tree
//    and note its contents.
//
// Postconditions:
// 1. Inserts a cut-list-item folder feature containing the specified
//    weldment body.
// 2. Expand the Cut-List-Item1 folder in the Solid Bodies(1) folder
//    in the the FeatureManager design tree to verify step 1.
//
// NOTE: Because this part is used elsewhere,
// do not save changes.
//----------------------------------------------------------------------------
```

using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swconst;

using System;

namespace InsertWeldmentCutList2_CSharp.csproj

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}partial
class SolidWorksMacro

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ModelDoc2
Part;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Body2[]
obj = new Body2[1];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Object[]
v;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}long
i;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
void Main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Part
= (ModelDoc2)swApp.**ActiveDoc**;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}v
= (object[])((PartDoc)Part).**GetBodies2**(0, true);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}for
(i = 0; i <= v.GetUpperBound(0); i++)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}obj[i]
= (Body2)v[i];

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Feature
cutListFeature = default(Feature);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}cutListFeature
= Part.**FeatureManager**.InsertWeldmentCutList2(obj);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}public
SldWorks swApp;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}

}
