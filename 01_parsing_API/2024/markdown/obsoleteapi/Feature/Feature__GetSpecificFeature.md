---
title: "Feature::GetSpecificFeature"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Feature/Feature__GetSpecificFeature.htm"
---

# Feature::GetSpecificFeature

This method is obsolete and has been superseded
by[Feature::GetSpecificFeature2](sldworksAPI.chm::/Feature/Feature__GetSpecificFeature2.htm).

Description

This
method gets the interface for the specific feature type.

Syntax (OLE Automation)

retval
= Feature.GetSpecificFeature ()

(Table)=========================================================

| Return: | (LPDISPATCH)
retval | Dispatch
pointer to a feature of unknown type |
| --- | --- | --- |

Syntax (COM)

status
= Feature->IGetSpecificFeature ( &retval )

(Table)=========================================================

| Output: | (LPUNKNOWN)
retval | Pointer
to the feature of unknown type |
| --- | --- | --- |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

(Table)=========================================================

| If... | Then... |
| --- | --- |
| You start with a Feature object and want to get a more specific object | A call to Feature::GetSpecificFeature is required.
If you have the more specific object, then a call to QueryInterface in
C++ or assignment to a Feature-typed variable allows an application to
get back to the Feature object. |
| You are writing a Dispatch application | You can use Feature::GetTypeName to recognize
the type of Dispatch object returned so you can call the appropriate properties
and methods for that object. |
| You are writing a COM application | You can use the return value with QueryInterface to determine the object
returned. |
| No interface exists | This method returns NULL. |

For many feature types, this method returns NULL because there is no
specific object for that type (for example, extrusion or cut features).
For all functions that return objects, always check whether the return
value is NULL before you try to use it.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Feature_Object$$**$$swSelectType_e$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Feature\Feature__GetSpecificFeature.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="QueryInterface_Example$$**$$Get_Info_on_Plane/Axis_Example$$**$$Get_Feature_and_SubFeature_Example$$**$$QueryInterface_Example$$**$$Get_Sketches_Example$$**$$SectionProperties_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\Feature\Feature__GetSpecificFeature.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
