---
title: "AttributeDef::CreateInstance2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AttributeDef/AttributeDef__CreateInstance2.htm"
---

# AttributeDef::CreateInstance2

This method is obsolete and has been superseded by[AttributeDef::CreateInstance3](AttributeDef__CreateInstance3.htm)

Description

This method creates an Attribute defined by this AttributeDef on the
specified entity. Afterkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}an
Attribute is added to an entity, the attribute and its information is
stored with the document upon saving.

Syntax (OLE Automation)

retval = AttributeDef.CreateInstance2
( ownerDoc, ownerEntity, nameIn, options)

(Table)=========================================================

| Input: | (LPDISPATCH) ownerDoc | Document whose FeatureManager design tree this attribute is to be added. |
| --- | --- | --- |
| Input: | (LPDISPATCH) ownerEntity | Entity to which the Attribute will be applied or NULL for the document |
| Input: | (BSTR) nameIn | Name to be given to this Attribute instance |
| Input: | (long) options | Creation control options |
| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the newly created attribute instance |

Syntax (COM)

status = AttributeDef->ICreateInstance2
( ownerDoc, ownerEntity, nameIn, options, &retval )

(Table)=========================================================

| Input: | (LPMODELDOC) ownerDoc | Document whose FeatureManager design tree this attribute is to be added |
| --- | --- | --- |
| Input: | (LPENTITY) ownerEntity | Entity to which the Attribute will be applied or NULL for the document |
| Input: | (BSTR) nameIn | Name to be given to this Attribute instance |
| Input: | (long) options | Creation control options |
| Output: | (LPATTRIBUTE) retval | Pointer to the newly created attribute instance |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The attribute is created as a feature and displayed in the FeatureManager,
which means that the name specified in nameIn must be unique in the FeatureManager
for the document.

You can create attributes on Entity objects (such as Faces and Edges),
on Features, or on the document itself.

Setting or clearing bits in the options argument controls the creation
of the attribute:

(Table)=========================================================

| Bit | Value | Meaning |
| --- | --- | --- |
| 1 | 1 | Attribute is created hidden in the FeatureManager (see Feature::SetUIState) |
|  | 0 | Attribute is created visible in the FeatureManager |

For example, Options = 1 creates an attribute that is hidden in the
FeatureManager view.

NOTE:By default, SolidWorks adds attributes only to the active configuration.
SolidWorks adds the attribute to all other configurations as a suppressed
feature. You can unsuppress the attribute by selecting it with ModelDoc2::SelectById
and calling ModelDoc2::EditUnsuppressDependent2. If you want to add your
attributes to a non-active configuration, then the user needs to edit
the properties of that particular configuration and make sure that theSuppress New Featuresoption is
disabled.

Attributes are not supported on Library Features or Library Feature
Parts. If you add an attribute to an entity, SolidWorks strips the Attribute
feature from the entity if the entity is included in your export to a
Library Feature or Library Feature Part.

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\AttributeDef\AttributeDef__CreateInstance2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
