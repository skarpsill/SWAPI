---
title: "ModelDoc::GetPopupMenuMode"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetPopupMenuMode.htm"
---

# ModelDoc::GetPopupMenuMode

This
method is obsolete and has been superseded by[ModelDoc2::GetPopupMenuMode](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetPopupMenuMode.htm).

Description

This method determines the current pop-up menu
mode.

Syntax (OLE Automation)

retval = ModelDoc.GetPopupMenuMode ( )

(Table)=========================================================

| Return: | (int) retval | Current pop-up menu mode |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->GetPopupMenuMode ( &retval
)

(Table)=========================================================

| Output: | (int) retval | Current pop-up menu mode |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

When the user clicks the a right-mouse button (RMB)
on an entity in the graphics window, the user is presented with one of
two distinct menu sets. These menu sets are defined as mode 0 and mode
1:

##### Mode

0 – Default RMB
mode. This will present user with options toSelect
Other, manipulate the view, access the properties dialog of the
selected item, and so on.

1 – The user is
presented with a limited set of choices includingSelect
OtherandClear Selection.
This mode is seen typically when a SolidWorks dialog is active and the
user is restricted to entity selection.

Using ModelDoc::SetPopupMenuMode, your application
can simulate the same RMB menu behavior as SolidWorks. If you have a dialog
that requires user selection of entities, you can set the popup menu mode
to 1 to simulate SolidWorks behavior. You should always set the menu mode
back to its previous value. Call ModelDoc::GetPopupMenuMode to determine
the previous value prior to calling ModelDoc::SetPopupMenuMode.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ModelDoc::SetPopupMenuMode$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__GetPopupMenuMode.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
