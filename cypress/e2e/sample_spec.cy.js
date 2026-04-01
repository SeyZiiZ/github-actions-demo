describe('Sample Test', () => {
  it('should visit example.com and check the title', () => {
    cy.visit('https://example.com')
    cy.title().should('include', 'Example Domain')
  })

  it('should find the main heading', () => {
    cy.visit('https://example.com')
    cy.get('h1').should('contain', 'Example Domain')
  })

  it('should have a link to more information', () => {
    cy.visit('https://example.com')
    cy.get('a').should('have.attr', 'href')
  })
})
