---
title: "AttributeDef::CreateInstance"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AttributeDef/AttributeDef__CreateInstance.htm"
---

# AttributeDef::CreateInstance

This method is obsolete and has been superseded
by[AttributeDef::CreateInstance2](AttributeDef__CreateInstance2.htm).

Description

This method creates an Attribute defined by this AttributeDef on the
specified entity. After an Attribute is added to an entity, the attribute
and its information is stored with the document upon saving.

Syntax (OLE Automation)

retval
= AttributeDef.CreateInstance ( ownerDoc, ownerEntity, nameIn)

(Table)=========================================================

| Input: | (LPDISPATCH)
ownerDoc | Document
whose FeatureManager design tree this attribute is to be added |
| --- | --- | --- |
| Input: | (LPDISPATCH)
ownerEntity | Entity
to which the attribute will be applied or NULL for the document |
| Input: | (BSTR)
nameIn | Name
to be given to this attribute instance (see Remarks ) |
| Return: | (LPDISPATCH)
retval | Pointer
to a dispatch object, the newly created attribute instance |

Syntax (COM)

status
= AttributeDef->ICreateInstance ( ownerDoc, ownerEntity, nameIn, &retval
)

(Table)=========================================================

| Input: | (LPMODELDOC)
ownerDoc | Document
whose FeatureManager design tree this attribute is to be added |
| --- | --- | --- |
| Input: | (LPENTITY)
ownerEntity | Entity
to which the attribute will be applied or NULL for the document |
| Input: | (BSTR)
nameIn | Name
to be given to this attribute instance (see Remarks ) |
| Output: | (LPATTRIBUTE)
retval | Pointer
to the newly created attribute instance |
| Return: | (HRESULT)
status | S_OK
if successful |

Remarks

The attribute is created as a feature and displayed in the FeatureManager
design tree, which means that the name specified in nameIn must be unique
in the FeatureManager design tree for the document.

You can create attributes on entity objects such as faces and edges,
on features, or on the document itself.

NOTE:By default, SolidWorks adds attributes only to the active configuration.
SolidWorks adds the attribute to all other configurations as a suppressed
feature. You can unsuppress the attribute by selecting it with ModelDoc2::SelectById
and calling ModelDoc2::EditUnsuppressDependent2. If you want to add your
attributes to a non-active configuration, then the use must edit the properties
of that particular configuration and make sure that theSuppress
New Featuresoption is disabled.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1323" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="AttributeDef_Object$$**$$ZCreateAttribute$$**$$ZGetAttribute$$**$$ZAccessorByCreate$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\AttributeDef\AttributeDef__CreateInstance.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
