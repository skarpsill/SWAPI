---
title: "eDSheet Class"
project: ""
interface: "eDSheet"
member: ""
kind: "class"
source: "emodeltoolkit/eDSheet/eDSheet_Class.htm"
---

# eDSheet Class

(Generated Script Links)========================================

(Generated Code)================================================

(WARNING: DO NOT EDIT OR DELETE THIS SECTION!)==================

begin!kadov{{===================================================

}}end!kadov=====================================================

(==============================================================)

(Table)=========================================================

| See
Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Contains one or more views.

#### Header file code

class eDSheet : public[eDObject](../eDObject/eDObject_Class.htm)

{

public:

eDOutcomebegin!kadov{{}}end!kadovCreateBaseView( constECHARbegin!kadov{{}}end!kadov*viewname,[eDView](../eDView/eDView_Class.htm)*& view
); //Creates a base view

eDOutcomebegin!kadov{{}}end!kadovCreateView( constECHARbegin!kadov{{}}end!kadov*viewname, const[eDTransform3d](../eDTransform3d/eDTransform3d_Class.htm)&viewtransf,[eDView](../eDView/eDView_Class.htm)*&
view ); //Creates a view. The optional view transform argument will only
position the view if it contains[eDShellList](../eDShellList/eDShellList_Class.htm)geometry; that is, facet data added through[eDBody::CreateShellList](../eDBody/eDBody_Class.htm)and added to a view through[eDView::CreatePart](../eDView/eDView_Class.htm).
In all other instances, the view border will size automatically to hold
other geometry (lines, points, curves, etc.) that are specified in global
coordinates.

};

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
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
<param name="Items" value="DocumentStructureClasses$$**$$eDDrawings$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\eModelToolkit\eDSheet\eDSheet_Class.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan

begin!kadov{{

}}end!kadov

kadov_tag{{<implicit_p>}}

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
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
<param name="Items" value="ZGeteDSheet$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2007\eModelToolkit\eDSheet\eDSheet_Class.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>

Metadata type="DesignerControl" endspan
