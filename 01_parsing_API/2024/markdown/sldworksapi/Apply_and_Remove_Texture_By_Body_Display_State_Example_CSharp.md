---
title: "Apply and Remove Texture By Body Display State Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Apply_and_Remove_Texture_By_Body_Display_State_Example_CSharp.htm"
---

# Apply and Remove Texture By Body Display State Example (C#)

## Apply and Remove Texture By Body Display State (C#)

This example shows how to apply and remove texture to and from a body
by a display state.

```
//--------------------------------------------------
// Preconditions: Verify that the specified part to open
// and texture exist.
//
// Postconditions:
// 1. Opens the specified part and applies texture to the
//    selected body.
// 2. In the IDE, click the Continue button
//    at System.Diagnostics.Debugger.Break().
// 3. Removes texture from selected body.
// 4. To verify, click the Stop Debugging button in the
//    IDE to stop execution of the macro and click anywhere
//    in the graphics area.
//    - or -
//    If the Stop Debugging button is grayed out, click
//    anywhere in the graphics area.
//----------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;

namespace SetRemoveTextureByDisplayStateBodyCSharp.csproj
```

```vb
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SelectionMgr swSelMgr = default(SelectionMgr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDocExtension swModelDocExt = default(ModelDocExtension);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Body2 body = default(Body2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Texture texture = default(Texture);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelView modelview = default(ModelView);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool status = false;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string displayState = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int errors = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int warnings = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}string namStr = null;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Open document and select a body
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\SOLIDWORKS 2018\\samples\\tutorial\\multibody\\multi_bridge.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModelDocExt = (ModelDocExtension)swModel.Extension;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}status = swModelDocExt.SelectByID2("hub", "SOLIDBODY", 0, 0, 0, false, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSelMgr = (SelectionMgr)swModel.SelectionManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}body = (Body2)swSelMgr.GetSelectedObject6(1, -1);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Set texture on selected body in the
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// specified display state
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}displayState = "<Default>_Display State 1";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}namStr = "<SystemTexture>\\images\\textures\\pattern\\checker2.jpg";
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}texture = (Texture)swModelDocExt.CreateTexture(namStr, 5, 45, false);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}status = body.SetTextureByDisplayState(displayState, texture);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Redraw the window view
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}modelview = (ModelView)swModel.ActiveView;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}modelview.GraphicsRedraw(null);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Examine the selected body to verify
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// that the specified texture was set
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// In the IDE, click the Continue button to resume
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// running macro
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}System.Diagnostics.Debugger.Break();

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Remove texture from body by display state
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}status = swModelDocExt.SelectByID2("hub", "SOLIDBODY", 0, 0, 0, false, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}body = (Body2)swSelMgr.GetSelectedObject6(1, -1);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}status = body.RemoveTextureByDisplayState(displayState);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
