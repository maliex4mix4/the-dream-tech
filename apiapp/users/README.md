# User Account
This shows a documentation for the user Account.

## Things to happen
- User creates an account.
- Users can sign up for an Account.
- Vendors can Login to their account only if the have a User account.
- Vendors can Sign up for an account only if the have a User account.
- Email Confirmation is sent upon account creation.
- Welcome Email is sent After registration process.

## EndPoints

**Note** All APi should follow this particular format.

**Note** All api should return in format:
`
{
  "success": #True or False,
  "payload": {
    #data goes in here.
  },
  "info": #provides additional info about the error.,
}

`
**Note** info is not necessarily sent always.

### User Create account.

- {base_url}/api/auth/users/ [method=POST]

### User LOgin account

- {base_url}/api/auth/users/login [method=POST]

### Email activation

- {base_url}/api/auth/email/confirm/<key> [method=GET]
- Create new_activation
- {base_url}/api/auth/email/confirm/  [method=POST] and takes only email in the form field.
