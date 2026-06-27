---
title: "Feature::GetTypeName"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Feature/Feature__GetTypeName.htm"
---

# Feature::GetTypeName

This method is obsolete and has been superseded
by[Feature::GetTypeName2](sldworksAPI.chm::/Feature/Feature__GetTypeName2.htm).

Description

This
method gets the type of feature.

Syntax (OLE Automation)

retval = Feature.GetTypeName ()

(Table)=========================================================

| Return: | (BSTR) retval | Feature type as defined in BodyFeatures_e |
| --- | --- | --- |

Syntax (COM)

status = Feature->GetTypeName (
&retval )

(Table)=========================================================

| Output: | (BSTR) retval | Feature type as defined in BodyFeatures_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For example, if this feature is a plane, then
this method returns swTnRefPlane, which is equivalent to the string value
"RefPlane".

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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Feature_Object$$**$$ZGetNames$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Feature\Feature__GetTypeName.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
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
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Get_Info_on_Plane/Axis_Example$$**$$Get_Feature_and_SubFeature_Example$$**$$Entity Select Example$$**$$Traverse_Assembly_Component_Feature_Example$$**$$EXGetSelectedFeature$$**$$EXTraverseCosmeticThreads$$**$$EXCustomBendDeduction$$**$$EXFacesWithFeatures$$**$$EXSelectOriginAssemblyComponent$$**$$EXGetParentFeatures$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2008\obsoleteapi\Feature\Feature__GetTypeName.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
